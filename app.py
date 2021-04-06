import Adafruit_DHT
from flask import Flask

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

app = Flask(__name__)

@app.route('/temperature')
def temperature():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return 'Temperature in taverna is {:.2f}C with humidity {:.2f}%'.format(temperature,humidity)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
