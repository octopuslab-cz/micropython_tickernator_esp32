# micropython_tickernator_esp32

##
Basic modules from: OctopusLAB frame work (ver.2)

https://github.com/octopuslab-cz/esp32_micropython_framework

---

## MicroPython 
- latest, stable, vanila: ver. v1.20: 

https://micropython.org/download/esp32/ ->

https://micropython.org/resources/firmware/esp32-20230426-v1.20.0.bin

---

## Deploy (mip):

```
from time import sleep
import network
import mip

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sleep(5)

print("wifi connect")
wlan.connect('ssid', 'password')
sleep(5)

mip.install("github:octopuslab-cz/micropython_tickernator_esp32", target=".")
```

---

## 3D stl model
https://www.thingiverse.com/thing:5950832
