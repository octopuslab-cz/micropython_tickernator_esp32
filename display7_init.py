from time import sleep
from machine import Pin, SPI
from components.display7 import Display7


#I2C:
I2C_SCL_PIN = const(22)
I2C_SDA_PIN = const(21)

# SPI:
SPI_CLK_PIN  = const(18)
SPI_MISO_PIN = const(19)
SPI_MOSI_PIN = const(23)
SPI_CS0_PIN  = const(5)

DISPLAY_INTENSITY = 2 # 6 default


# spi_init
spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(SPI_CLK_PIN), mosi=Pin(SPI_MOSI_PIN))
ss = Pin(SPI_CS0_PIN, Pin.OUT)


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
