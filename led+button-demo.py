#!/usr/bin/python3
#
# Demonstrate use of Wombat board buttons and LEDs
#
# light LED D1 when button S1 is pressed and
# light LED D4 when button S2 is pressed
#
# using wombat.py module readbutton() and setled() functions
#
#   v1.0    28/4/15
#
#   David Meiklejohn
#   Gooligum Electronics
#

from wombat import *

try:
  while True:
    setled(1, readbutton(1))
    setled(4, readbutton(2))

except KeyboardInterrupt:
  cleanup()

