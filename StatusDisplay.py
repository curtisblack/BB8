import os
import re
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class StatusDisplay:
    def __init__(self, bb8):
        #LCD.__init__(self, 0x20)
        self.display = Adafruit_SSD1306.SSD1306_128_32(rst=16)
        self.display.begin()
        self.image = Image.new('1', (self.display.width, self.display.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()

        self.BB8 = bb8
        self.showIP = True
        self.lastUpdateTime = 0

    def Update(self):
        t = time.time()
        if t > self.lastUpdateTime + 2:
            #self.draw.rectangle((0, 0, self.display.width, self.display.height), outline=0, fill=0)
            ip = ("IP: " + self.BB8.Network.IP) if self.BB8.Network.IP else "No Network"
            ssid = ("SSID: " + self.BB8.Network.SSID) if self.BB8.Network.SSID else "No Network"
            #if self.lastIP != ip:
            self.draw.rectangle((0, 0, self.display.width, self.display.height), outline=0, fill=0)
            self.draw.text((0, 0), ip if self.showIP else ssid, font=self.font, fill=255)
            self.display.image(self.image)
            self.display.display()
            self.showIP = not self.showIP
            #cpu = "CPU: " + os.popen("top -bn1 | tail -n +8 | awk '{ SUM += $(NF-3) } END { printf \"%.0f%%\", SUM }'").read()
            #mem = "Mem: " + os.popen("free -m | awk 'NR==2{printf \"%s/%s MB %.0f%%\", $3,$2,$3*100/$2 }'").read()
            #disk = "Disk: " + os.popen("df -h | awk '$NF==\"/\"{printf \"%.2g/%d GB %s\", $3,$2,$5}'").read()
            #self.draw.text((0, -1), ip, font=self.font, fill=255)
            #self.draw.text((0, 7), cpu, font=self.font, fill=255)
            #self.draw.text((0, 15), mem, font=self.font, fill=255)
            #self.draw.text((0, 23), disk, font=self.font, fill=255)
            #self.display.image(self.image)
            #self.display.display()
            self.lastUpdateTime = t

    def Exit(self):
        self.display.clear()
        self.display.display()

    def format(self, number):
        if number >= 100:
            return str(int(round(number)))
        elif number >= 10:
            return "%.1f" % number
        else:
            return "%.2f" % number
