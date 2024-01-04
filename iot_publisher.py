import paho.mqtt.client as mqtt
import time
import random
import json

# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code " + str(rc))
#     client.subscribe("test/topic")

# client = mqtt.Client()
# client.on_connect = on_connect

# client.connect("localhost", 1883, 60) # Connect to your MQTT broker (replace "localhost" with the broker's address if different)

# # Loop to simualate continuous data publishing
# while True:
#    distance_beacon_1 = random.uniform(1, 30)
#    distance_beacon_2 = random.uniform(1, 30)
#    distance_beacon_3 = random.uniform(1, 30)

#    # Create a payload string with the distances
#    payload = f"{distance_beacon_1}, {distance_beacon_2}, {distance_beacon_3}"
#    client.publish("beacon/distances", payload)
#    print(f"Published: {payload}")

#    time.sleep(2) # Wait for 2 seconds before sending next data


broker_address = "localhost"
port = 1883
topic = "iot/sensors/data"  

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client("PythonPublisher")
client.on_connect = on_connect

client.connect(broker_address, port, 60)

while True:

    distance_beacon_1 = random.uniform(1, 30)
    distance_beacon_2 = random.uniform(1, 30)
    distance_beacon_3 = random.uniform(1, 30)

    # Create a JSON object
    payload = json.dumps({
        "beacon_1_distance": distance_beacon_1,
        "beacon_2_distance": distance_beacon_2,
        "beacon_3_distance": distance_beacon_3,
    })

    client.publish(topic, payload)
    print(f"Message Sent: {payload}")
    time.sleep(5)  # Publish every 5 seconds