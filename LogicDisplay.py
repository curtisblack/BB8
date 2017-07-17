import time
import random

class LogicDisplay:
    def __init__(self, strip, offset):
        self.strip = strip
        self.offset = offset

    def SetColor(self, r, g, b):
        for i in range(3):
            self.strip.setPixelColorRGB(self.offset + i, r, g, b)
        self.strip.show()

    def SetColors(self, colors):
        for i, c in enumerate(colors):
            self.strip.setPixelColorRGB(self.offset + i, c[0], c[1], c[2])
        self.strip.show()

class FrontTopLogicDisplay(LogicDisplay):
    def __init__(self, strip):
        LogicDisplay.__init__(self, strip, 3)
        self.State = "default"
        self.nextUpdate = 0

    def SetDefault(self):
        self.SetColor(100, 100, 100)
        self.State = "default"

    def SetR2D2(self):
        self.State = "r2d2"
        self.nextUpdate = time.time()

    def Update(self):
        if self.State == "r2d2":
            t = time.time()
            if t > self.nextUpdate:
                self.nextUpdate = t + 0.1
                choices = [(0, 0, 255), (255, 255, 255)]
                colors = [choices[random.randint(0, len(choices) - 1)] for i in range(3)]
                self.SetColors(colors)

class FrontBottomLogicDisplay(LogicDisplay):
    def __init__(self, strip):
        LogicDisplay.__init__(self, strip, 6)
        self.State = "default"
        self.nextUpdate = 0

    def SetDefault(self):
        self.SetColor(0, 0, 0)
        self.State = "default"

    def SetR2D2(self):
        self.State = "r2d2"
        self.nextUpdate = time.time()

    def Update(self):
        if self.State == "r2d2":
            t = time.time()
            if t > self.nextUpdate:
                self.nextUpdate = t + 0.1#random.random() / 10
                choices = [(0, 0, 255), (255, 255, 255)]
                colors = [choices[random.randint(0, len(choices) - 1)] for i in range(3)]
                self.SetColors(colors)

class SideLogicDisplay(LogicDisplay):
    def __init__(self, strip):
        LogicDisplay.__init__(self, strip, 0)
        self.State = "default"
        self.nextUpdate = 0

    def SetDefault(self):
         self.SetColor(0, 50, 120)
         self.State = "default"

    def SetR2D2(self):
        self.State = "r2d2"
        self.nextUpdate = time.time()

    def Update(self):
        if self.State == "r2d2":
            t = time.time()
            if t > self.nextUpdate:
                self.nextUpdate = t + 0.1#random.random() / 10
                choices = [(255, 0, 0), (0, 255, 0), (255, 255, 0)]
                colors = [choices[random.randint(0, len(choices) - 1)] for i in range(3)]
                self.SetColors(colors)
