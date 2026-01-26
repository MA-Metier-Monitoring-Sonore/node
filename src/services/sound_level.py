import alsaaudio
import audioop
import math
import os

import src.config.config as config

class SoundLevel:

    def __init__(self):
        self.sample_width = config.SAMPLE_WIDTH
        self.db_offset = config.DB_OFFSET

        self.inp = alsaaudio.PCM(
            alsaaudio.PCM_CAPTURE,
            alsaaudio.PCM_NORMAL,
            device=os.getenv("DEVICE"),
            channels=config.CHANNELS,
            rate=config.RATE,
            format=alsaaudio.PCM_FORMAT_S16_LE,
            periodsize=config.PERIODSIZE,
        )

    def get_dbA(self):
        """Reading audio data from the microphone and convert in decibels"""

        length, data = self.inp.read()
        if length == 0 or not data:
            return None

        rms = audioop.rms(data, self.sample_width)
        print("RMS:", rms)
        if rms <= 1:
            return -90.0

        db = 20 * math.log10(rms / 32768) 

        dbA = db + 1.7 + self.db_offset

        return dbA