from LED import LED

class ProcessStateIndicator:
    def __init__(self):
        self.red = LED(17)
        self.green = LED(27)
        self.blue = LED(22)

    def SetBrightness(self, brightness):
        self.red.SetBrightness(brightness)
        self.green.SetBrightness(brightness)
        self.blue.SetBrightness(brightness)

    def SetValue(self, r, g, b):
        self.red.SetValue(r)
        self.green.SetValue(g)
        self.blue.SetValue(b)

    def SetDefault(self):
        self.SetValue(255, 255, 255)
