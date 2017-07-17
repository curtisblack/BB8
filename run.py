#!/usr/bin/env python

import os
import sys
import time
import fcntl
import signal
import pygame
import traceback
from BB8 import BB8

procs = os.popen("sudo ps ax | grep python").read().split("\n")
for proc in procs:
    if "run.py" in proc:
        pid = int(proc.lstrip(" ").split(" ")[0])
        if pid != os.getpid():
            os.system("sudo kill " + str(pid))
            time.sleep(1)

bb8 = BB8()

def handler(signal, frame):
    bb8.Exit()
    sys.exit(0)

signal.signal(signal.SIGTERM, handler)

def running():
    bb8.Update()
    return True

def run(script):
    exec(open(os.path.realpath(script)).read(), { "running": running, "bb8": bb8 })

running()

for script in sys.argv[1:]:
    run(script)

clock = pygame.time.Clock()
while running():
    clock.tick(50)

