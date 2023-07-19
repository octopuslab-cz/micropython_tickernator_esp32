from time import sleep
from ticker import Ticker, bitcoin_usd
from ticker import time_init, get_hh_mm_ss, disp8_pause, show_moving
from octopus_lib import getFree
from components.display8 import Display8
from utils.wifi_connect import WiFiConnect

print("OctopusLAB - bitcoin tickernator")
t = Ticker()

DELAY_BTC = 20 # 15 sec.

t.print_config_info()
spi, ss = t.spi_init()

print("[Display init]")
d8 = Display8(spi, ss) # 8 x 7segment display init

d8.write_to_buffer('octopus')
d8.display()
sleep(3)
d8.intensity = 7
disp8_pause(d8)
d8.intensity = t.intensity # DISPLAY_INTENSITY

print("[WiFi connect]")
net = WiFiConnect()
net.connect()
d8.show("WiFi")
sleep(2)

if not net.isconnected():
    net.sta_if.disconnect() # hard reconect
    net.connect()

rtc = time_init(t.timezone)

# =================== main loop ==========
while True:
    getFree(True)
    btc = bitcoin_usd()
    print(btc)
    #disp8_pause(d8)
    show_moving(d8,str(int(btc)))
    
    for i in range(3):
        d8.show(str(int(btc)))
        sleep(DELAY_BTC)
        d8.show("USD-BTC")
        sleep(1.5)
    
        for t in range(10):
            d8.show(get_hh_mm_ss(rtc))
            sleep(1)
