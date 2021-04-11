import json
import requests
import socket
import time

PORT=2003
SERVER="localhost"

while(True):
    r = requests.get(url = "http://192.168.1.102:5000/temperature")
    data = r.json()
    temperature = data['temperature']
    humidity = data['humidity']
    timestamp = int(time.time())
    message_temperature = '%s %s %d\n' % ('taverna.temperature', temperature, timestamp)
    message_humidity = '%s %s %d\n' % ('taverna.humidity', humidity, timestamp)
    sock = socket.socket()
    sock.connect((SERVER, PORT))
    sock.sendall(message_temperature.encode('utf-8'))
    sock.sendall(message_humidity.encode('utf-8'))
    sock.close()
    time.sleep(60)


