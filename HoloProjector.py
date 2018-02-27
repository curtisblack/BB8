import time
import random

class HoloProjector:
    def __init__(self, bb8, strip):
        self.bb8 = bb8
        self.strip = strip
        self.offset = 9
        self.State = "default"
        self.nextUpdate = 0

    def SetColor(self, r, g, b):
        for i in range(7):
            self.strip.setPixelColorRGB(self.offset + i, r, g, b)
        self.strip.show()
        self.State = "color"
        self.bb8.Sound.Hologram.stop()

    def SetDefault(self):
        self.SetColor(0, 0, 0)
        self.State = "default"

    def SetMessage(self):
        self.State = "message"
        self.nextUpdate = time.time()
        self.bb8.Sound.Hologram.play(-1)

    def Update(self):
        if self.State == "message":
            t = time.time()
            if t > self.nextUpdate:
                self.nextUpdate = t + random.random() / 20
                choices = [(0, 0, 0), (0, 127, 255), (255, 255, 255)]
                for i in range(7):
                    c = choices[random.randint(0, len(choices) - 1)]
                    self.strip.setPixelColorRGB(self.offset + i, c[0], c[1], c[2])
                self.strip.show()
