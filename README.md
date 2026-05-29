# Assignemnt 2: IoT  Environmental Monitor 
## Student Name: Stephen Adamson
## Student ID: W20119151

# Overview
This project is a simple IoT connected device system using a Raspberry Pi and SenseHAT sensor to create an environmental monitor.
It collects environmental data (temperature and humidity), processes it locally, sends it using MQTT messaging, and displays results in a subscriber dashboard while logging data for history.

This system provides real time collection of environmental data using the Sense HAT sensor on a Raspberry Pi. 
The data is processed continuously and transmitted between components using MQTT publish/subscribe communication. The messages use JSON format to ensure consistent and readable data exchange.

The system demonstrates a IoT architecture including:

- Sensor Layer
- Processing Layer
- Networking Layer
- Application Layer

# Tools, Technology and Equipment

## Hardware:
- Raspberry Pi 4
- SenseHAT
- Micro SD card

## Software:
- Python 3
- MQTT (Mosquitto broker)
- Paho MQTT library
- JSON
- Linux (Raspberry Pi OS)
 The Raspberry Pi was set up with headless configuration.

# System Architecture



## Sensor
The Sense HAT is used to collect temperature and humidity data at 5 second intervals. 
The SenseHAT hardware is also used for physical feedback, displaying system status through LED colours to indicate conditions. 
Temperature readings will be displayed as "HOT HOT HOT!", "COSY", or "FINE"

## Processing
They system processes the data and calculates an average temperature reading.  Processed data detects the comfort level in the room or immediate surroundings of the device (HOT, COSY, or FINE).

## Networking
MQTT was installed and is used for communication between devices.
-Protocol is MQTT
-Mosquito Broker is used
- Topic - Telemetry/topic
- message format uses JSON

Example message
`Sent {'temperature': 34.66, 'humidity': 33.05, 'average_temperature': 34.66, 'temp_status': 'HOT HOT HOT!'}
Sent {'temperature': 34.66, 'humidity': 33.0, 'average_temperature': 34.66, 'temp_status': 'HOT HOT HOT!'}` 

#Application layer
The file subscriber.py was created to receive and display MQTT messages. 
The application provides a terminal based dashboard that displays the liev sensor readings to the user. All incoming data received is stored in a JSON log file sensor_data.json.


# How to use the environmental monitor system
 The following steps outline how to run the environmental monitoring system on the RPi
1. After logging into the Raspberry Pi device, start MQTT broker
	`sudo systemctl start mosquitto`
2. Run the subscriber 
	'python3 subscriber.py`
3. Open a second terminal window and run the publisher
	`python3 publisher.py`
The user will then see data readings from the device refreshing every 5 seconds. subscriber.py will display the data in json format.

# Project folder structure
iotassignment/
├── publisher.py
├── subscriber.py
├── sensor_data.json
├── README.md

# Reflection
The project allowed me to demonstrate knowledge of the subject matter and incorporate learnings from other modules on the course. The subject matter is challenging and so the objective was to deliver a functional IoT system as oulined. 
This project demonstrates how differant layers can work together to deliver a solution. Physical hardware collects ebvironmental data. MQTT is used as the network protocol to transmit the data between the publisher and subscriber components in this project. The logic applied to the sensor data allows system states and average tremperature calculations to be processed.
All documentation is stored on GitHub. Commits were used to track progress however, not until a late stage in the project with work having taken place without regular commits.
#Video
https://youtu.be/jW0iV0ZxuIY
