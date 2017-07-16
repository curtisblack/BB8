from RPi.GPIO import *

class LED:
    def __init__(self, pin):
        setmode(BCM)
        self.pin = pin
        setup(self.pin, OUT)
        self.pwm = PWM(self.pin, 1000)
        self.pwm.start(0)
        self.value = 0
        self.brightness = 255

    def Update(self):
        self.pwm.ChangeDutyCycle(100 * self.value * self.brightness / (255 * 255))

    def SetValue(self, value):
        self.value = value
        self.Update()

    def Off(self):
        self.SetValue(0)

    def On(self):
        self.SetValue(255)

    def Toggle(self):
        self.value = 255 if self.value < 127 else 0
        self.Update()

    def SetBrightness(self, brightness):
        self.brightness = brightness
        self.Update()
        
