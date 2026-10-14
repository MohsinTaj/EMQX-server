import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/temperature"

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="python-publisher"
)

client.connect(BROKER, PORT, 60)

client.loop_start()

print("Connected to EMQX Broker")

try:
    while True:

        data = {
            "device": "sensor01",
            "temperature": random.randint(20, 40),
            "humidity": random.randint(40, 80)
        }

        payload = json.dumps(data)

        info = client.publish(
            TOPIC,
            payload,
            qos=1
        )

        info.wait_for_publish()

        print("Published:", payload)

        time.sleep(5)

except KeyboardInterrupt:
    print("Stopping publisher...")

finally:
    client.disconnect()
    client.loop_stop()
