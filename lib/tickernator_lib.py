# OctopusLAB tickernator - time and Bitcoin price
from time import sleep
import urequests, json
import utime
from ntptime import settime
from machine import RTC


__version__ = "2.3.0"


def time_init(zone=1):
    print("time_init")
    # if wifi.on
    settime()
    rtc = RTC()
    utc_shift = zone

    tm = utime.localtime(utime.mktime(utime.localtime()) + utc_shift*3600)
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    rtc.datetime(tm)
        
    print("--- time: " + get_hh_mm_ss(rtc))
    return rtc


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
    for i in range(len(txt)):
         d7.show(txt[:i])
         sleep(0.2)


# note: 10-20 sec. pause is required
def bitcoin_usd():
    res = urequests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
    btcusd = res.json()['quotes']["USD"]["price"]
    return float(btcusd)
