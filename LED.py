from RPi.GPIO import *

class LED:
    def __init__(self, pin):
        setmode(BCM)
        self.pin = pin
        setup(self.pin, OUT)
        self.pwm = PWM(self.pin, 1000)
        self.pwm.start(0)
        self.Value = 0
        self.Brightness = 255

    def Update(self):
        self.pwm.ChangeDutyCycle(100 * self.Value * self.Brightness / (255 * 255))

    def SetValue(self, value):
        self.Value = max(0, min(value, 255))
        self.Update()

    def Off(self):
        self.SetValue(0)

    def On(self):
        self.SetValue(255)

    def Toggle(self):
        self.Value = 255 if self.Value < 127 else 0
        self.Update()

    def SetBrightness(self, brightness):
        self.Brightness = brightness
        self.Update()
        
