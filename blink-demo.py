#!/usr/bin/python3
#
# Demonstrate use of Wombat board LEDs
# (the obligatory "flash an LED demo")
#
# flashes LEDs D2 and D3 at 1 Hz
#
# using wombat.py module setled() function
#
#   v1.0    28/4/15
#
#   David Meiklejohn
#   Gooligum Electronics
#

import time
from wombat import *

try:
  while True:
    setled(2, 0)        # LED D2 off, D3 on
    setled(3, 1)
    time.sleep(0.5)     #   for 0.5 sec

    setled(2, 1)        # LED D2 on, D3 off
    setled(3, 0)
    time.sleep(0.5)     #   for 0.5 sec

except KeyboardInterrupt:
  cleanup()

