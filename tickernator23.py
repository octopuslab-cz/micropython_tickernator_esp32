from time import sleep
from machine import RTC
from display7_init import disp7_init, disp7_pause, show_moving, DISPLAY_INTENSITY
from utils.wifi_connect import WiFiConnect
from tickernator_lib import __version__, time_init, add0, get_hh_mm_ss, bitcoin_usd
from config import Config


print("--- Tickernator23 ---")
print("lib. version:",__version__)


c_intensity = DISPLAY_INTENSITY
c_timezone = 1

keys = ["ver","intensity","timezone"]
try:
    conf = Config("ticker",keys)
    c_ver = conf.get("ver")     # config version
    c_intensity = conf.get("intensity")
    c_timezone = conf.get("timezone")
except:
    print("err: read config - exist?")

print("-"*20)
print("[Config]")
print("-"*20)
print("ver",c_ver)
print("intensity",c_intensity)
print("timezone",c_timezone)
print("-"*20)

DELAY_BTC = 20 # 15 sec.
DISPLAY_INTENSITY = c_intensity


print("[Display init]")
d7 = disp7_init()   # 8 x 7segment display init
d7.write_to_buffer('octopus')
d7.display()
sleep(3)
disp7_pause(d7)

print("[WiFi connect]")
net = WiFiConnect()
net.connect()
d7.intensity = DISPLAY_INTENSITY 
d7.show("WiFi")
sleep(3)

if not net.isconnected():
    net.sta_if.disconnect() # hard reconect
    net.connect()

rtc = time_init(c_timezone)


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
