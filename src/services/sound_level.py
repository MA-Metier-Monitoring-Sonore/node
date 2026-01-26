import alsaaudio
import audioop
import math
import os

import src.config.config as config

class SoundLevel:

    def __init__(self):
        self._sample_width = config.SAMPLE_WIDTH
        self._db_offset = config.DB_OFFSET

        self._inp = alsaaudio.PCM(
            alsaaudio.PCM_CAPTURE,
            alsaaudio.PCM_NORMAL,
            device=os.getenv("DEVICE"),
            channels=config.CHANNELS,
            rate=config.RATE,
            format=alsaaudio.PCM_FORMAT_S16_LE,
            periodsize=config.PERIODSIZE,
        )

    def get(self):
        """Reading audio data from the microphone and convert in decibels"""

        length, data = self._inp.read()
        if length == 0 or not data:
            return None

        rms = audioop.rms(data, self._sample_width)
        
        if rms <= 1:
            return 0

        db = 20 * math.log10(rms / 32768) 

        dbA = db + 1.7 + self._db_offset

        return dbA
