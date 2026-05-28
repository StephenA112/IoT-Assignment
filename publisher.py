from sense_hat import SenseHat
import paho.mqtt.client as mqtt
import json
import time

# Define colours
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#initialise sense hat, hardware
sense = SenseHat()

#MQTT client
USER_ID = "sadamson"

client = mqtt.Client(client_id=f"{USER_ID}-edge")
client.connect("localhost", 1883, 60)

temp_readings = []

##def get_environmental_data():
   # temp = sense.get_temperature()
   # humidity = sense.get_humidity()
    #return temp, humidity

def get_comfort_level(temp, humidity):
    if 20 <= temp <= 26 and 40 <= humidity <= 60:
        return "COSY"
    elif temp > 28 or humidity > 70:
        return "HOT HOT HOT!"
    else:
        return "FINE"

while True:

    temp = round(sense.get_temperature(), 2)
    humidity = round(sense.get_humidity(), 2)

    temp_readings.append(temp)

    if len(temp_readings) > 5:
        temp_readings.pop(0)

    avg_temp = round(sum(temp_readings) / len(temp_readings), 2)

    comfort = get_comfort_level(temp, humidity)

   # if temp > 28:
    #    status = "HOT HOT HOT!"
#	color = RED
 #       sense.clear(255, 0, 0)
  #  else:
   #     status = "COMFORTABLE :)"
#	color = GREEN
 #       sense.clear(0, 255, 0)

    if comfort == "HOT HOT HOT!":
       sense.show_message("HOT HOT HOT!", text_colour=RED)
       sense.clear(255, 0, 0)

    elif comfort == "COSY":
       sense.show_message("COSY :)", text_colour=BLUE)
       sense.clear(0, 0, 255)

    else:
       sense.show_message("FINE", text_colour=GREEN)
       sense.clear(0, 255, 0)

	#Display on LED matrix
       sense.show_message("T:{:.1f}C".format(temp), text_colour=RED)
       sense.show_message("H:{:.1f}%".format(humidity), text_colour=BLUE)

    #MQTT payload
    payload = {
        "temperature": temp,
        "humidity": humidity,
        "average_temperature": avg_temp,
        "temp_status": comfort
    }

    client.publish("telemetry/topic", json.dumps(payload))

    print("Sent", payload)

#5 second delay before next reading

    time.sleep(5)
