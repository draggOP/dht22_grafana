import json
import requests
import socket
import time

PORT=2003
SERVER="localhost"

while(True):
    r = requests.get(url = "http://192.168.1.102:5000/temperature")
    data_p0 = r.json()
    temperature_p0 = data_p0['temperature']
    humidity_p0 = data_p0['humidity']
    timestamp = int(time.time())
    message_temperature_p0 = '%s %s %d\n' % ('p0.temperature', temperature_p0, timestamp)
    message_humidity_p0 = '%s %s %d\n' % ('p0.humidity', humidity_p0, timestamp)
    
    r = requests.get(url = "http://192.168.1.184:80")
    data_p2 = r.json()
    temperature_p2 = data_p2['temperature']
    message_temperature_p2 = '%s %s %d\n' % ('p2.temperature', temperature_p2, timestamp)
    
    sock = socket.socket()
    sock.connect((SERVER, PORT))
    sock.sendall(message_temperature_p0.encode('utf-8'))
    sock.sendall(message_temperature_p2.encode('utf-8'))
    sock.sendall(message_humidity_p0.encode('utf-8'))
    sock.close()
    time.sleep(60)


