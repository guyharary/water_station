#IMPORTS
import sqlite3 as sql
#from socket import *
import datetime
import socket
import time


# DATA
BUFFSIZE = 2048


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
with sql.connect(db_file) as conn:
    conn.execute(sql_create_table_water_station)



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 54322        # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print("Waiting for connection...")

    conn, addr = s.accept()
    with conn:
        print('Connection established via: ', addr)
        while True:
            time.sleep(3)
            data = conn.recv(BUFFSIZE)
            data = data.decode()
            print(data)
            if not data:
                s.listen()
                print("No data")
            # socket.setblocking(False) --> trying to keep the loop alive without exiting.
            conn.sendall(data.encode())
            x = data.split()
            id = (x[0])
            alarm1 = (x[1])
            alarm2 = (x[2])
            last_date = (x[3] + " " + x[4])
            print(last_date)

            with sql.connect(db_file) as conn:
                conn.execute(q, (x[0], x[1], x[2], x[3] + " " + x[4]))