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
TOPIC = "CH/Vaud/Ste-Croix/" + CLIENT_ID
TOPIC_CONFIG = TOPIC + "/config"
TOPIC_SOUNDLEVEL = TOPIC + "/soundlevel"

async def main():
    """Main asynchronous function to handle MQTT connection and subscription."""
    client = aiomqtt.Client(BROKER_HOST)
    interval = 5
    sound_level = SoundLevel()

    async with aiomqtt.Client(BROKER_HOST) as client:
        Logger.info("Connected to MQTT broker")

        await client.publish(
            TOPIC_CONFIG,
            json.dumps({
                "lon": os.getenv("DEVICE_LON"),
                "lat": os.getenv("DEVICE_LAT"),
            }),
            qos=1,
            retain=True
        )

        while True:
            try:
                await client.publish(
                    TOPIC_SOUNDLEVEL,
                    json.dumps({
                        "lvl": sound_level.get(),
                    })
                )
                await asyncio.sleep(0.1)

            except aiomqtt.MqttError:
                Logger.error(f"Connection lost; Reconnecting in {interval} seconds ...")
                await asyncio.sleep(interval)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
