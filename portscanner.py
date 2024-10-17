#!/bin/python3



import sys
import socket
from datetime import datetime

pa = open('ip.txt', "r")
vish = []
vish.append(pa.read(13).strip())
vish.append(pa.read(13).strip())
vish.append(pa.read(14).strip())
z,y, x = vish


target = socket.gethostbyname(z)
targets = socket.gethostbyname(x)
targetss = socket.gethostbyname(y)

# add pretty banner
print("-" * 50)
print("scanning:" + target)
print("Process started Time:" + str(datetime.now()))
print("-" * 50)


for port in range(0, 1023):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f'port {port} is open')
    s.close()

print(f"  Another port is not active or closed.")

print("-" * 50)
print("scanning:" + targets)
print("Time:" + str(datetime.now()))
print("-" * 50)

for ports in range(0, 1023):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    results = ss.connect_ex((targets, ports))
    if results == 0:
        print(f"port{ports} is open")
    ss.close()
print('port is closed or not active')

print("-" * 50)
print("scanning:" + targetss)
print("Process started Time:" + str(datetime.now()))
print("-" * 50)

for ports in range(10, 1000):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    results = ss.connect_ex((targetss, ports))
    if results == 0:
        print(f"port{ports} is open")
    ss.close()

print(f'{vish} is enough to function process ')