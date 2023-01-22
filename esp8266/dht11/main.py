from machine import Pin
import utime
import dht

sensordht = dht.DHT11(Pin(15)) # declaro el objeto y el pin a utilizar

while True:
    sensordht.measure() #actualiza los valores de temp y humedad
    print("Temp= "+str(sensordht.temperature())+" Hum= "+str(sensordht.humidity())) #imprimo los valores
    utime.sleep(1) # sensor toma 1 segundo en tomar los valores...
    
    