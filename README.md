# dht22_grafana

This repository contains scripts used to poll data from a humidity/temperature sensor attached to a raspberry pi and read the results from a grafana dashboard:
* `app.py` webapp that runs on the raspberry pi with the sensor and exposes the humidity/temperature data in json format on the `temperature` endpoint.
* `data_feeder.py` python script that sends a request to the `temperature` endpoint exposed by `app.py` and inserts the data in the graphite database.
* `docker-compose.yml` used to start grafana and graphite services used to display the data.
