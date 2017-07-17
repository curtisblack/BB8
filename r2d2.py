import time
import random

bb8.SetR2D2()
bb8.SetBrightness(255)

nextSound = time.time()
nextLight = time.time()

while running():
    t = time.time()
    
    if t > nextLight:
        nextLight = t + random.randint(1, 10)
        bb8.HoloProjector.SetColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #if t > nextSound:
    #    nextSound = t + random.randint(10, 20)
    #    bb8.Sound.Play("Generic")

    #if bb8.Network.Changed("R2D2"):
    #    if bb8.Network.IsConnected("R2D2"):
    #        r2.Sound.Play("Happy")
    #    else:
    #        r2.Sound.Play("Sad")
