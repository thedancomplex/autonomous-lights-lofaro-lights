#!/usr/bin/python3
from pyHS100 import SmartBulb
from pprint import pformat as pf
import random as r
import time as t

#bulb = SmartBulb("10.66.3.17")
#print("Hardware: %s" % pf(bulb.hw_info))
#print("Full sysinfo: %s" % pf(bulb.get_sysinfo()))
#bulb.turn_on()
#bulb.hsv = (180, 100, 100)

i = 0
while True:
  h = r.random() * 270
  h = int(h)
          #h = 100
  s = r.random() * 100
  s = int(s)
  s = 100
  for y in range(1,4):
    for x in range(17,25):
    #for x in range(1,35):
        addr = "10.66."+str(y)+"."+str(x)
        print(addr)
        if ( ( x == 24 ) & (y == 1 ) ):
            pass
        else:
         try:
          b = SmartBulb(addr)
          b.turn_on()
#          b.turn_off()
#          b.turn_off()
#          b.turn_off()
#          b.turn_off()
          #s = 100
          b.hsv = (h,s, 100)
         except:
          pass
  print(i)
  i += 1
  t.sleep(1.0)


