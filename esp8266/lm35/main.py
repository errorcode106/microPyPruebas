from machine import ADC # import las conexiones ADC 
import time

valorAnalogico = ADC(0) # declaramos una variable para almacenar la lectura del pin 0
conversion_factor = 3.3/1024  # convertir el voltaje para la lectura de  10 bits = 1024 q es la lectura del sensor

while True:
    
    voltage_leido = valorAnalogico.read()
    conversion_voltage = voltage_leido * conversion_factor
    tempCentigrados = conversion_voltage/(10.0/1000) # pasa a grados centigrados
    
    print("temperature: ",tempCentigrados,"ºC")
    
    time.sleep(2)
    