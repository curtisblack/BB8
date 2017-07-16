class HoloProjector:
    def __init__(self, strip):
        self.strip = strip
        self.offset = 9

    def SetColor(self, r, g, b):
        for i in range(7):
            self.strip.setPixelColorRGB(self.offset + i, r, g, b)
        self.strip.show()

    def SetDefault(self):
        self.SetColor(255, 255, 255)
