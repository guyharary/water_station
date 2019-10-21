#!/usr/bin/env python3

import socket

HOST = ''  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    s.settimeout(3)
    listclient=[]
    while 1:
        conn = None
        try:
            conn, addr = s.accept()
            listclient.append(conn)
        except:
            print("no connection")

        if conn:
            with conn:
                print('Connected by', conn.getsockname())
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    else:
                        print(data)
                        conn.send(data)