from time import sleep
from machine import Pin, SPI
from components.display7 import Display7
from utils.pinout import set_pinout
from utils.octopus_lib import spi_init

DISPLAY_INTENSITY = 2 # 6 default

pinout = set_pinout()
spi = spi_init()

ss = Pin(pinout.SPI_CS0_PIN, Pin.OUT)
#spi.deinit() #print("spi > close")

def disp7_init():
    d7 = None
    try:
        d7 = Display7(spi, ss) # 8 x 7segment display init
        # d7.write_to_buffer('octopus')
        # d7.display()
    except:
        print("Err. Display7 init")
    return d7


def disp7_pause(d7,ch="-",sl=0.1):
    d7.intensity = 7
    for i in range(9):
        #print(i, ch*i)
        d7.show(ch*i)
        sleep(sl)
    d7.intensity = DISPLAY_INTENSITY


# simple "moving text" - max. displ. size (8)
def show_moving(d7,txt):
    for i in range(len(txt)):
         d7.show(txt[:i])
         sleep(0.2)
