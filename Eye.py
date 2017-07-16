from LED import LED

class Eye:
    def __init__(self):
        self.LED1 = LED(21)
        self.LED2 = LED(20)
        self.LED3 = LED(16)
        self.LED4 = LED(12)
        self.LED5 = LED(26)
        self.LED6 = LED(19)

    def SetBrightness(self, brightness):
        self.LED1.SetBrightness(brightness)
        self.LED2.SetBrightness(brightness)
        self.LED3.SetBrightness(brightness)
        self.LED4.SetBrightness(brightness)
        self.LED5.SetBrightness(brightness)
        self.LED6.SetBrightness(brightness)

    def SetDefault(self):
        self.LED1.On()
        self.LED2.Off()
        self.LED3.Off()
        self.LED4.Off()
        self.LED5.Off()
        self.LED6.Off()
