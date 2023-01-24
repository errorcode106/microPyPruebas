from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,scl=Pin(5),sda=Pin(4),freq=200000)
oled = SSD1306_I2C(128,64,i2c)
oled.text("hola ssd1306",0,11)
oled.show()