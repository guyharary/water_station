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
with sql.connect(db_file) as conn:
    conn.execute(sql_create_table_water_station)



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 54321        # Port to listen on

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
                #break
            conn.sendall(data.encode())
            x = data.split()
            id = (x[0])
            alarm1 = (x[1])
            alarm2 = (x[2])
            last_date = [''.join(x[3])]
            #test_list[5: 8] = [''.join(test_list[5: 8])]

            with sql.connect(db_file) as conn:
                #conn.execute(q, (x[0], x[1], x[2], x[3:]))
                conn.execute(q, (id, alarm1, alarm2, last_date)) # this line drops the code after executing
                                                                 # comes back to line 50. need to create a loop.





















#s = "string 1"
#print(s[:3]) # will print the entire string up to the character at index 3 (not including that character)
# therefore it will print: str

#print(s[2:]) # will print the string from the character at index 2 (included) up to the end of the string (including the last character
# therefire it will print: ring 1

#print(s[1:3])
# will print from character at index 1 up to the character at index 3 not including.
# so it will print: tr












#sql_insert_water_station = """
#INSERT INTO STUDENT VALUES
#(?, ?, ?, ?);
#"""