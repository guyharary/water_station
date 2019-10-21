import socket as sock
import datetime
import socket
import time
import sys

BUFSIZE = 1024

if len(sys.argv) != 2:
    print("Please pass a filename")
    exit(1)

filename = sys.argv[1]
with open(filename) as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    content.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    print(' '.join(content))
    # print(datetime.datetime.now().strftime('%Y-%M-%d %H:%m'))

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888  # The port used by the server

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while True:
                s.send(' '.join(content).encode())
                data = s.recv(1024)
                data = data.decode()
                print('Received', repr(data))

    except KeyboardInterrupt:
        print('Fuck you, bye..')
        exit(1)

    except:
        pass
