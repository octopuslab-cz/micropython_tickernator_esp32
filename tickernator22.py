from time import sleep
# from utils.octopus import disp7_init
from display7_init import disp7_init, disp7_pause, DISPLAY_INTENSITY
from utils.octopus_api import bitcoin_usd
# from utils.octopus_lib import w
from utils.wifi_connect import WiFiConnect

print("ticker22 - init")

d7 = disp7_init()   # 8 x 7segment display init
d7.write_to_buffer('octopus')
d7.display()
sleep(3)

net = WiFiConnect()
net.connect()
d7.intensity = DISPLAY_INTENSITY 
d7.show("WiFi")
sleep(3)

if not net.isconnected():
    # hard reconect
    net.sta_if.disconnect()
    net.connect()


while True:
    btc = bitcoin_usd()
    print(btc)
    disp7_pause(d7)
    d7.show(str(int(btc)))
    sleep(60) # 60
    d7.show("USD-BTC")
    sleep(2)
