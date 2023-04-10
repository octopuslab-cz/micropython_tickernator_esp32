from time import sleep
from ticker import Ticker
from ticker import time_init, bitcoin_usd, get_hh_mm_ss, disp7_pause, show_moving
from components.display7 import Display7
from utils.wifi_connect import WiFiConnect


print("OctopusLAB - bitcoin tickernator")
t = Ticker()

DELAY_BTC = 20 # 15 sec.
DISPLAY_INTENSITY = t.intensity

t.print_config_info()
spi, ss = t.spi_init()

print("[Display init]")
d7 = Display7(spi, ss) # 8 x 7segment display init

d7.write_to_buffer('octopus')
d7.display()
sleep(3)
d7.intensity = 7
disp7_pause(d7)
d7.intensity = DISPLAY_INTENSITY

print("[WiFi connect]")
net = WiFiConnect()
net.connect()
d7.intensity = DISPLAY_INTENSITY 
d7.show("WiFi")
sleep(3)

if not net.isconnected():
    net.sta_if.disconnect() # hard reconect
    net.connect()

rtc = time_init(t.timezone)


# =================== main loop ==========
while True:
    btc = bitcoin_usd()
    print(btc)
    #disp7_pause(d7)
    show_moving(d7,str(int(btc)))
    
    for i in range(3):
        d7.show(str(int(btc)))
        sleep(DELAY_BTC)
        d7.show("USD-BTC")
        sleep(1.5)
    
        for t in range(10):
            d7.show(get_hh_mm_ss(rtc))
            sleep(1)
