# (c) OctopusLAB 2016-23 - class Ticker
__version__ = "2.0.0"
# HW ESP32 + display8

from machine import Pin, SPI #, I2C
from time import sleep, sleep_ms
from micropython import const
from config import Config
# from components.led import Led
# from components.rgb import Rgb
# from components.analog import Analog
from octopus_lib import getFree, getUid, add0 
from components.display8 import Display8
from machine import RTC
import urequests, json
from ntptime import settime
import utime

DEBUG = True



class Ticker:
    def __init__(self, hw=2):
        if DEBUG: print("[init] class constructor")
        self.hw = hw # hw ver 1+ / 2config
        self.uid = getUid()
        
        #I2C:
        self.I2C_SCL_PIN = const(22)
        self.I2C_SDA_PIN = const(21)

        # SPI:
        self.SPI_CLK_PIN  = const(18)
        self.SPI_MISO_PIN = const(19)
        self.SPI_MOSI_PIN = const(23)
        self.SPI_CS0_PIN  = const(5)
        
        self.DISPLAY_INTENSITY = 2 # 6 default
                
        # pinout - ADC
        self.PIN_A0 = const(35) # NTC
        self.PIN_A1 = const(34) # 32
        self.PIN_A2 = const(39) # 33 # ad voltage
        self.PIN_A3 = const(33) # PWM_IN 39>33
        
        # pinout - RGB-WS
        self.PIN_WS = const(25)
        
        keys = ["ver","intensity","timezone","coins","note"]
        try:
            conf = Config("ticker",keys)
            self.ver = conf.get("ver")     # config version
            self.intensity = conf.get("intensity") # display intensity
            self.timezone = conf.get("timezone") # 110 temp.start
            self.coins = conf.get("coins") # TODO / nice to have 
            self.note = conf.get("note")   # hw note
            self.conf = conf
        except:
            print("err: read config - exist?")
               
    
    def print_config_info(self):
        print("-"*26)
        print("--- ticker json config ---")
        print("class ticker ver.", __version__)
        print("uID:",self.uid)
        getFree(True)
        print("-"*26)
        print("  version    ", self.ver)
        print("  intensity  ", self.intensity)
        print("  timezone   ", self.timezone)
        print("  coins (*)  ", self.coins)
        print("  note       ", self.note)
        print("-"*26)
        
    """
    def set_intensity(self, value):  self.intensity = value
    def set_timezone(self, value):  self.timezone = value
        
    
    def save_config(self):
        self.conf.set("intensity",self.intensity)
        self.conf.set("timezone",self.timezone)
        self.conf.set("note",self.note)        
        self.conf.save() # save the configuration file with the new settings
    
    
    def init_ir(self):
        print("- ir-temp")
        print("-- i2c_init - sensor")
        self.sensor = None
        try:
            i2c = i2c_init()
            sleep(0.5)
            self.sensor = mlx90614.MLX90614(i2c)
        except:
            print("err: i2c IR sensor - connect?")
        return self.sensor
    """
    
    def spi_init(self):
        # spi_init
        spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(self.SPI_CLK_PIN), mosi=Pin(self.SPI_MOSI_PIN))
        ss = Pin(self.SPI_CS0_PIN, Pin.OUT)
        if DEBUG: print("[SPI init]")
        return spi, ss
# -----------------------------------

"""
def i2c_init(HW_or_SW=0,freq=100000):
    # from utils.pinout import set_pinout
    # pinout = set_pinout()
    I2C_SDA_PIN, I2C_SCL_PIN = const(21), const(22)
    # HW_or_SW: HW 0 | SW 1
    i2c = I2C(HW_or_SW, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN), freq=freq)
    return i2c


def disp7_init(spi,ss):
    d7 = None
    try:
        d7 = Display7(spi, ss) # 8 x 7segment display init
    except:
        print("Err. Display7 init")
    return d7
"""

def disp8_pause(d8,ch="-",sl=0.1):
    for i in range(9):
        #print(i, ch*i)
        d8.show(ch*i)
        sleep(sl)    


# simple "moving text" - max. displ. size (8)
def show_moving(d8,txt):
    for i in range(len(txt)):
         d8.show(txt[:i])
         sleep(0.2)


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

"""
def add0(sn): # 1 > 01 - TODO better;)
    ret_str=str(sn)
    if int(sn)<10:
       ret_str = "0"+str(sn)
    return ret_str
"""

def get_hh_mm_ss(rtc):
    hh=add0(rtc.datetime()[4])
    mm=add0(rtc.datetime()[5])
    ss=add0(rtc.datetime()[6])
    return hh+"-"+mm+"-"+ss


def show_moving(d8, txt):
    for i in range(len(txt)):
         d8.show(txt[:i])
         sleep(0.2)


# note: 10-20 sec. pause is required
def bitcoin_usd():
    btcusd = 666
    try:
        res = urequests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
        btcusd = res.json()['quotes']["USD"]["price"]
    except:
        print("err: bitcoin_usd API / wifi connect?")
    return float(btcusd)
