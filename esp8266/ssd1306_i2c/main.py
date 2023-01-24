from machine import Pin, I2C
from ssd1306 import SSD1306_I2C # https://github.com/stlehmann/micropython-ssd1306.git
 
i2c=I2C(Pin(5),Pin(4))  # GPIO 5 = SCL ; GPIO 4 = SDA
oled = SSD1306_I2C(128,64,i2c)
oled.text("hola ssd1306",0,0)
oled.show()