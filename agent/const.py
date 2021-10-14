import sys

PAYLOAD_PATH = ".bin/"
PAYLOAD_NAME = '.payload.app' if sys.platform == 'darwin' else '.payload.exe'
BLOCK_SIZE = 65535

STAGER_CODE = 0
CONN_CODE = 1
