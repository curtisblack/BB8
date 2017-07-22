import os
import time
import math
import wave
import numpy
import random
from pygame import mixer

class Sound(object):
    def __init__(self):
        self.directory = "/home/pi/BB8/Sounds"
        mixer.init()
        self.file = None
        self.current = 0
        self.start = 0
        self.Volume = 50
        self.Hologram = mixer.Sound(self.directory + "/Hologram/314.wav")

    #@property
    def get_Volume(self):
        return mixer.music.get_volume()

    #@Volume.setter
    def set_Volume(self, value):
        volume = max(0, min(100, value))
        mixer.music.set_volume(value / 100.0)

    Volume = property(get_Volume, set_Volume)

    def PlayFile(self, file):
        if self.file != None:
            self.file.close()
        self.file = wave.open(file, 'r')
        self.current = 0
        mixer.music.load(file)
        mixer.music.set_volume(1)
        mixer.music.play()
        self.start = time.time()

    def Play(self, directory, number=None):
        d = os.path.join(self.directory, directory)
        files = sorted(os.listdir(d))
        if number == None:
            number = random.randint(0, len(files) - 1)
        self.PlayFile(os.path.join(d, files[number]))

    def GetAmplitude(self):
        if self.file == None:
            return 0
        p = time.time() - self.start
        now = int((p - 0.5) * self.file.getframerate())
        if now - self.current - 1 < 1:
            return 0
        self.file.readframes(now - self.current - 1)
        self.current = now
        data = numpy.fromstring(self.file.readframes(1), dtype=numpy.int16)
        if len(data) > 0:
            x = float(sum([abs(int(d)) for d in data])) / len(data) / 2**12
            return 0.5 + math.atan((x - 0.5) * 10) / 2.7
        return 0
