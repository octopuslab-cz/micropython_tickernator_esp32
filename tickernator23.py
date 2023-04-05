from time import sleep
# from utils.octopus import disp7_init
from display7_init import disp7_init, disp7_pause, DISPLAY_INTENSITY
from utils.octopus_api import bitcoin_usd
# from utils.octopus_lib import w
from utils.wifi_connect import WiFiConnect
from ntptime import settime
from machine import RTC

DELAY_BTC = 20 # 15 sec.

print("ticker23 - init")

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


def add0(sn): # 1 > 01 - TODO better;)
    ret_str=str(sn)
    if int(sn)<10:
       ret_str = "0"+str(sn)
    return ret_str


def get_hh_mm_ss(rtc):
    hh=add0(rtc.datetime()[4])
    mm=add0(rtc.datetime()[5])
    ss=add0(rtc.datetime()[6])
    return hh+"-"+mm+"-"+ss

def show_moving(d7, txt):
    for i in range(5):
         d7.show(txt[:i])
         sleep(0.2)


# time_init
rtc = RTC()
settime() # if wifi.on
print("--- time: " + get_hh_mm_ss(rtc)) 



while True:
    btc = bitcoin_usd()
    print(btc)
    #disp7_pause(d7)
    show_moving(d7,str(btc))
    
    for i in range(3):
        d7.show(str(int(btc)))
        sleep(DELAY_BTC)
        d7.show("USD-BTC")
        sleep(1.5)
    
        for t in range(10):
            d7.show(get_hh_mm_ss(rtc))
            sleep(1)
        