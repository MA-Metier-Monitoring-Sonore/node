import alsaaudio
import audioop
import math
import time

import config

class SoundLevel:

    def __init__(self):
        self.sample_width = config.SAMPLE_WIDTH
        self.db_offset = config.DB_OFFSET

        self.inp = alsaaudio.PCM(
            alsaaudio.PCM_CAPTURE,
            alsaaudio.PCM_NORMAL,
            device=config.DEVICE,
            channels=config.CHANNELS,
            rate=config.RATE,
            format=alsaaudio.PCM_FORMAT_S16_LE,
            periodsize=config.PERIODSIZE,
        )

    def read_dbA(self):
        """Reading audio data from the microphone and convert in decibels"""

        length, data = self.inp.read()
        if length == 0 or not data:
            return None

        rms = audioop.rms(data, self.sample_width)
        print("RMS:", rms)
        if rms <= 1:
            return -90.0

        # dB brut 
        db = 20 * math.log10(rms / 32768) 

        # Pondération A simplifiée 
        dbA = db + 1.7 + self.db_offset

        return dbA


    def get(self):
        """Show decibels"""

        try:
            while True:
                dbA = self.read_dbA()
                if dbA is not None:
                    print(f"Decibels : {dbA:.1f} dB")
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("Stopping the script.")

if __name__ == "__main__":
    SoundLevel().get()
