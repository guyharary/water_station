import socket as sock
import datetime
import socket
import time

BUFSIZE = 1024

with open("station_status.txt") as f:
  content = f.readlines()
  content = [x.strip() for x in content]
  content.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
  print(' '.join(content))
  #print(datetime.datetime.now().strftime('%Y-%M-%d %H:%m'))




HOST = ''          # The server's hostname or IP address
PORT = 54321       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.send(' '.join(content).encode())
        data = s.recv(1024)
        data = data.decode()
        print('Received', repr(data))
        time.sleep(2)














#last_date = datetime.datetime.now().strftime('%Y-%M-%d %H:%m')
#date = [y.strip() for y in last_date]
#print(date)


#rearrange_list
#mylist = ['a', 'b', 'c', 'd', 'e']
#myorder = [3, 2, 0, 1, 4]
#mylist = [mylist[i] for i in myorder]
#print(mylist)         # prints: ['d', 'c', 'a', 'b', 'e']



















#f = open("station_status.txt", "r")
#for x in f:
#  print(x)


#f = open("station_status.txt")
#msg = print(f.readline())
#print(msg)
#f.close()
