# Pi BME280 Environmental Sensor
This is a Pi3B based web server and BME280 environment sensor placed outdoors in an AREDN mesh node to serve out location environment statistics of temperature, pressure, and humidity.

## Prerequisites
- Pi 3B (best balance of capability, ethernet for mesh node, and low power consumption)
- i2c enabled on pi
- smbus for BME280 test C program
- Python3 and pip3
	- Flask, flask_sqlalchemy, SQLite
- nginx (optional, web proxy)
- gunicorn (optional, lightweight wsgi for productionalizing the app)

