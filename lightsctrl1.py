from datetime import datetime as dt
import asyncio #used to find kasa device
import kasa

light_sch = [10, 22] #10am to 10pm (10 hours)


devs = [x for x in asyncio.run(kasa.Discover.discover(timeout=1))]
strip = kasa.SmartStrip(devs[0])
asyncio.run(strip.update())


lights = strip.children[2] #plug 3

now = dt.now().time()
hr, min = now.hour, now.minute


if light_sch[0] <= hr < light_sch[1]:
	asyncio.run(lights.turn_on())
else: # otherwise turn them off
	asyncio.run(lights.turn_off())
