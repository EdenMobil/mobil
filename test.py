import paho.mqtt.client as mqtt
import time

client = None
topic = f"/edenmobil/cmd"

def connect():
    global client
    
    if client is None or not client.is_connected():
        broker = "10.0.4.246"
        print(broker)
        
        client = mqtt.Client(
            client_id="edenmobil",
            protocol=mqtt.MQTTv311,
            transport="tcp",
            callback_api_version=2
        )
        client.connect(broker)

connect()
client.publish(topic, "testing")