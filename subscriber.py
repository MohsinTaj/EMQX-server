import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/temperature"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to EMQX Broker")
        client.subscribe(TOPIC)
        print(f"Subscribed to: {TOPIC}")
    else:
        print(f"Connection failed: {reason_code}")


def on_message(client, userdata, message):
    print("\nNew MQTT Message Received")
    print("Topic:", message.topic)
    print("Payload:", message.payload.decode())


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="python-subscriber"
)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

print("Waiting for MQTT messages...")

client.loop_forever()
