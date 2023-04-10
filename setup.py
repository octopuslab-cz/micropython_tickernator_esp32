# setup / config - ver. 2022-10-22
from config import Config
from esp32 import NVS # Non-Volatile Storage - test


print("tickernator: Non-Volatile Storage")
setup2 = NVS("ticker") # test 2209
try:
   print("HW",setup2.get_i32("hw"))
except:
   print("setup.set_i32")
   setup2.set_i32("hw",2)

print()

print("tickernator: setup config")
# print(">>> conf.setup()")

keys = ["ver","intensity","timezone"]
conf = Config("ticker",keys)
conf.setup()
