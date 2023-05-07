from datetime import datetime as dt
import asyncio #used to find kasa device
import kasa

light_sch = [10, 22] #10am to 10pm (10 hours)



# find all devices
devs = [x for x in asyncio.run(kasa.Discover.discover(timeout=1))]
# this uses a list comprehension to find all devices on my network 
# this presumes the strip is the only kasa device on the network
strip = kasa.SmartStrip(devs[0])
asyncio.run(strip.update())
# see kasa library documentation for details: https://python-kasa.readthedocs.io/en/latest/smartdevice.html

# each plug is accessed using children
# assign names to each plug
lights = strip.children[2] #plug 3
# the lights must be plugged into port 3 for this to work

# get current hour and minute
now = dt.now().time()
hr, min = now.hour, now.minute

# if the current hour is within the light_schedule interval
# turn on lights
if light_sch[0] <= hr < light_sch[1]:
	asyncio.run(lights.turn_on())
else: # otherwise turn them off
	asyncio.run(lights.turn_off())
