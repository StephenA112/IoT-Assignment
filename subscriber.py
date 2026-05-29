import paho.mqtt.client as mqtt
import json

#MQTT callback
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

# Set up MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message

mqtt_client.connect("localhost", 1883, 60)
mqtt_client.subscribe("telemetry/topic") #subscribes MQTT client to topic

mqtt_client.loop_forever()
