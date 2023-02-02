from machine import Pin
import time

led = Pin (25,Pin.OUT) # indicamos el pin del led correspondiente en la placa de pico y q es de salida
while True: # ciclo infinito para apagar y encender el led
    led.value(1) # asignamos el valor 1 led encendido
    time.sleep(0.5) # espere 0.5 seg
    led.value(0) # asignamos el valor 0 led apagado
    time.sleep(0.5)
    
    