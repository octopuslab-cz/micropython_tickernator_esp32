# micropython_tickernator_esp32

##
OctopusLAB frame work (ver.1)

https://github.com/octopusengine/octopuslab/tree/master/esp32-micropython

TODO: Prepare for OctopusLAB frame work (ver.2)

https://github.com/octopuslab-cz/esp32_micropython_framework


---

## MicroPython 
- latest, stable, vanila: ver. v1.19.1 (2022-06-18).bin: https://micropython.org/download/esp32/

---

## Deploy:
https://github.com/octopuslab-cz/octopuslab-installer

```
from time import sleep

import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sleep(5)

print("wifi connect")
sleep(5)

import upip
upip.install('micropython-octopuslab-installer')

sleep(5)
print("deploy: .../download/micropython/tickernator.tar")
from lib import octopuslab_installer
deplUrl = "https://octopusengine.org/download/micropython/tickernator.tar"
octopuslab_installer.deploy(deplUrl)
```

---

## 3D stl model
https://www.thingiverse.com/thing:5950832
