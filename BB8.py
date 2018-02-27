import atexit
import time
import logging
import RPi.GPIO as GPIO
from LED import *
from Sound import *
from Network import *
from Eye import *
from LogicDisplay import *
from ProcessStateIndicator import *
from HoloProjector import *
from StatusDisplay import *
from neopixel import *

class BB8:
    def __init__(self):
        logging.basicConfig(format="%(levelname)s (%(asctime)s): %(message)s", datefmt="%I:%M:%S %p", level=logging.WARNING, filename="/var/tmp/BB8.log")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        #atexit.register(self.Exit)

        #self.Network = Network()
        self.strip = Adafruit_NeoPixel(3 + 3 + 3 + 7, 13, channel=1)
        #atexit.register(self.Exit)
        #print atexit._exithandlers
        self.strip.begin()

        atexit.register(self.Exit)

        self.Network = Network()
        self.Eye = Eye()
        self.ProcessStateIndicator = ProcessStateIndicator(self)
        self.FrontTopLogicDisplay = FrontTopLogicDisplay(self.strip)
        self.FrontBottomLogicDisplay = FrontBottomLogicDisplay(self.strip)
        self.SideLogicDisplay = SideLogicDisplay(self.strip)
        self.HoloProjector = HoloProjector(self, self.strip)
        self.StatusDisplay = StatusDisplay(self)
        self.Sound = Sound()

    def Exit(self):
        self.SetBrightness(0)
        self.StatusDisplay.Exit()
        GPIO.cleanup()

    def SetBrightness(self, brightness, limit = True):
        self.Eye.SetBrightness(brightness)
        self.ProcessStateIndicator.SetBrightness(brightness)
        self.strip.setBrightness(min(127, brightness / 2) if limit else brightness)
        self.strip.show()

    def SetDefault(self):
        self.Eye.SetDefault()
        self.ProcessStateIndicator.SetDefault()
        self.FrontTopLogicDisplay.SetDefault()
        self.FrontBottomLogicDisplay.SetDefault()
        self.SideLogicDisplay.SetDefault()
        self.HoloProjector.SetDefault()

    def SetR2D2(self):
        self.Eye.SetDefault()
        self.ProcessStateIndicator.SetR2D2()
        self.FrontTopLogicDisplay.SetR2D2()
        self.FrontBottomLogicDisplay.SetR2D2()
        self.SideLogicDisplay.SetR2D2()
        self.HoloProjector.SetDefault()

    def Update(self):
        self.Network.Update()
        self.ProcessStateIndicator.Update()
        self.FrontTopLogicDisplay.Update()
        self.FrontBottomLogicDisplay.Update()
        self.SideLogicDisplay.Update()
        self.HoloProjector.Update()
        self.StatusDisplay.Update()
