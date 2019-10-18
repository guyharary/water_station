#IMPORTS
import sqlite3 as sql
#from socket import *
import datetime
import socket
import time


# DATA
BUFFSIZE = 1024


# SQL_QUERYIES

db_file = "station_status.sqlite"

sql_create_table_water_station ="""
CREATE TABLE IF NOT EXISTS station_status (
    station_id TEXT,
    alarm1 INT,
    alarm2 INT,
    last_date TEXT, 
    PRIMARY KEY(station_id));
"""

q = """
insert or replace into station_status
values (?, ?, ?, ?)
"""

# check if database exists, if not create it
with sql.connect(db_file) as sql_conn:
    sql_conn.execute(sql_create_table_water_station)

HOST = ''  # Standard loopback interface address (localhost)
PORT = 54322        # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    s.settimeout(3)
    client_list = []
    print("Waiting for connection...")

    while True:
        conn = None
        try:
            conn, addr = s.accept()
            client_list.append(conn)
        except socket.timeout:                                   #except OSError:
            print("no connection timeout")                           #pass
        except:
            print("connection error")

        #else: #changeing else into a for loop
        for conn in client_list:
            conn.settimeout(1)
            print('Connection established via: ', addr)
            #print('Connection established via: ', conn.getsockname()) --> why different port?
            try:
                data = conn.recv(BUFFSIZE)
                data = data.decode() #decoding into string from bites
            except socket.timeout:
                print("no data")
            except:
                print("disconnect")
                client_list.remove(conn)
                conn.close()
                break
            else:
                if data:
                    #data = data.decode()
                    print(data)
            #if not data:
                #print("No data")

            conn.send(data.encode())
            x = data.split()
            #print(x)
            #print(client_list)
            id = (x[0])
            alarm1 = (x[1])
            alarm2 = (x[2])
            last_date = (x[3] + " " + x[4])
            #print(last_date)
            with sql.connect(db_file) as sql_conn:
                sql_conn.execute(q, (x[0], x[1], x[2], (x[3] + " " + x[4])))









#EXTRA HELP:

# def set_keepalive_linux(sock, after_idle_sec=1, interval_sec=3, max_fails=5):
#     """Set TCP keepalive on an open socket.
#
#     It activates after 1 second (after_idle_sec) of idleness,
#     then sends a keepalive ping once every 3 seconds (interval_sec),
#     and closes the connection after 5 failed ping (max_fails), or 15 seconds
#     """
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
#     sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
#     sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
#     sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)



#s = "string 1"
#print(s[:3]) # will print the entire string up to the character at index 3 (not including that character)
# therefore it will print: str

#print(s[2:]) # will print the string from the character at index 2 (included) up to the end of the string (including the last character
# therefire it will print: ring 1

#print(s[1:3])
# will print from character at index 1 up to the character at index 3 not including.
# so it will print: tr

#socket.setblocking(False) --> trying to keep the loop alive without exiting.

