"""Main module for MQTT client"""
import asyncio
import socket
import os
import json
import aiomqtt

from dotenv import load_dotenv
from services.logger import Logger
from services.sound_level import SoundLevel

load_dotenv()

CLIENT_ID = socket.gethostname()
BROKER_HOST = os.getenv("BROKER_HOST")
TOPIC = "CH/Vaud/Ste-Croix/" + CLIENT_ID + "/soundlevel"

async def main():
    """Main asynchronous function to handle MQTT connection and subscription."""
    client = aiomqtt.Client(BROKER_HOST)
    interval = 5
    sound_level = SoundLevel()

    async with aiomqtt.Client(BROKER_HOST) as client:
        Logger.info("Connected to MQTT broker")

        while True:
            try:
                await client.publish(
                    TOPIC,
                    json.dumps({
                        "client_id": CLIENT_ID,
                        "soundlevel": sound_level.get(),
                        "lon": os.getenv("DEVICE_LON"),
                        "lat": os.getenv("DEVICE_LAT"),
                    }),
                    qos=1,
                    retain=True
                )
                await asyncio.sleep(1)

            except aiomqtt.MqttError:
                Logger.error(f"Connection lost; Reconnecting in {interval} seconds ...")
                await asyncio.sleep(interval)

asyncio.run(main())
