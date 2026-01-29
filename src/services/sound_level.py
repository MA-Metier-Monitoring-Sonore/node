import alsaaudio
import threading
import audioop
import math
import os

import config.config as config

class SoundLevel:

    def __init__(self):
        self._sample_width = config.SAMPLE_WIDTH
        self._db_offset = config.DB_OFFSET
        self.current_db = None

        self._inp = alsaaudio.PCM(
            alsaaudio.PCM_CAPTURE,
            alsaaudio.PCM_NORMAL,
            device=os.getenv("DEVICE"),
            channels=config.CHANNELS,
            rate=config.RATE,
            format=alsaaudio.PCM_FORMAT_S16_LE,
            periodsize=config.PERIODSIZE,
        )

        # Start the background recording thread
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._capture_loop, daemon=True)
        self._thread.start()

    def _capture_loop(self):
        """Continuously reads from the mic to prevent buffer overflows."""
        while not self._stop_event.is_set():
            # This blocks until PERIODSIZE samples are ready
            length, data = self._inp.read()
            
            if length > 0:
                rms = audioop.rms(data, self._sample_width)
                rms = max(rms, 1)
                db = 20 * math.log10(rms / 32768)
                self.current_db = db + 1.7 + self._db_offset
            elif length == -32:
                # Handle Buffer Overrun: restart/continue
                continue

    def get(self):
        """Reading audio data from the microphone and convert in decibels"""
        return self.current_db
