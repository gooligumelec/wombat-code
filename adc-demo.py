#!/usr/bin/python3
#
# Demonstrate use of Wombat board analog inputs
#
# Read input 0 on MCP3008
# using wombat.py module readadc() function
#
#   v1.0    28/4/15
#
#   David Meiklejohn
#   Gooligum Electronics
#

import time
from wombat import readadc

adc_chan = 0        # use analog input CH0

try:
  while True:
    # get current value (0-1023) of ADC input
    adc_out = readadc(adc_chan)

    sensor_voltage = (adc_out * 3.3)/1024
    print("input voltage = %5.3f V" % (sensor_voltage))
    time.sleep(0.5)

except KeyboardInterrupt:
  print("done")

