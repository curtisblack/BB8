import time
import random
from LED import LED

class ProcessStateIndicator:
    def __init__(self, bb8):
        self.BB8 = bb8
        self.red = LED(5)
        self.green = LED(6)
        self.blue = LED(12)
        self.State = "default"
        self.nextUpdate = 0

    def SetBrightness(self, brightness):
        self.red.SetBrightness(brightness)
        self.green.SetBrightness(brightness)
        self.blue.SetBrightness(brightness)

    def SetValue(self, r, g, b):
        self.red.SetValue(r)
        self.green.SetValue(g)
        self.blue.SetValue(b)

    def SetDefault(self):
        self.SetValue(0, 0, 0)
        self.State = "default"

    def SetR2D2(self):
        self.State = "r2d2"
        self.nextUpdate = time.time()

    def Update(self):
        if self.State == "default":
            v = 255 * self.BB8.Sound.GetAmplitude()
            self.SetValue(v, v, v)
        elif self.State == "r2d2":
            t = time.time()
            if t > self.nextUpdate:
                self.nextUpdate = t + 3 * random.random()
                if self.red.Value == 255:
                    self.SetValue(0, 0, 255)
                else:
                    self.SetValue(255, 0, 0)
