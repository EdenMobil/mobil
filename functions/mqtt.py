from umqtt.robust import MQTTClient
from time import sleep

def setup_mqtt():
    print("Setting up MQTT connection...")
    client = MQTTClient("edenmobil", "127.0.0.1", port=1883)
    client.set_callback(on_message)

    try:
        client.connect()
        print("Successfully connected to MQTT broker")
        client.subscribe(b"/edenmobil/cmd")
        print("Subscribed to topic: edenmobil/cmd")
    except Exception as e:
        print("Failed to connect to MQTT broker: " + str(e))

    return client

def on_message(topic, msg):
    command = msg.decode("utf-8")
    print("Received command: " + command)