import json
import os

import paho.mqtt.client as mqtt


MQTT_HOST = os.getenv("MQTT_HOST", "127.0.0.1")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))


def on_connect(
    client, userdata, flags, reason_code, properties
):
    if reason_code == 0:
        print("Connected to EMQX")

        client.subscribe(
            "surveillance/+/detections",
            qos=1,
        )
    else:
        print(f"Connection failed: {reason_code}")


def on_message(client, userdata, message):
    event = json.loads(message.payload.decode("utf-8"))

    print("\nNew detection received:")
    print(json.dumps(event, indent=2))


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="surveillance-monitor-pc2",
)

username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")

if username:
    client.username_pw_set(username, password)

client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, 60)

client.loop_forever()