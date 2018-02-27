import time
import random

bb8.SetDefault()
bb8.SetBrightness(255)
bb8.Sound.Volume = 25

nextSound = time.time()
nextLight = time.time()

while running():
    t = time.time()
    
    if t > nextLight:
        nextLight = t + random.randint(2, 6)
        if random.randint(0, 5) == 0:
            bb8.HoloProjector.SetMessage()
        else:
            bb8.HoloProjector.SetDefault()
            #bb8.HoloProjector.SetColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    if t > nextSound:
        nextSound = t + random.randint(10, 20)
        bb8.Sound.Play("phrases")

    if bb8.Network.Changed("R2D2"):
        if bb8.Network.IsConnected("R2D2"):
            bb8.Sound.Play("Happy")
        else:
            bb8.Sound.Play("Frustrated")
