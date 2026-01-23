"""Main module for MQTT client"""
import threading
import sys
import socket
import os
import json
import paho.mqtt.client as mqtt

from dotenv import load_dotenv
from services.logger import Logger

load_dotenv()

client_id = socket.gethostname()
broker_host = os.getenv("BROKER_HOST")
broker_port = int(os.getenv("BROKER_PORT"))

def on_connect(*args, **kwargs):
    """Callback for when the client receives a CONNACK response from the server."""
    Logger.info("Connected to Broker.")

def on_connect_fail(*args, **kwargs):
    """Callback for when the client fails to connect to the server."""
    Logger.error(
        "Connection failed to Broker. Check network connection and/or broker host and port configuration."
    )

def publish():
    """Publish a message every 1 seconds."""
    topic = "CH/Vaud/Ste-Croix/" + client_id + "/soundlevel"
    payload = {
        "client_id": client_id,
        "soundlevel": 42
    }
    client.publish(topic, json.dumps(payload), qos=1, retain=True)
    threading.Timer(1, publish).start()

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id = client_id,
    protocol = mqtt.MQTTv5
)
client.on_connect = on_connect
client.on_connect_fail = on_connect_fail

try:
    client.connect(broker_host, broker_port, 60)
except OSError as e:
    Logger.critical(
        "Could not connect to Broker. Check network connection and/or broker host and port configuration."
    )
    sys.exit()

publish()

client.loop_forever(retry_first_connection=True)
