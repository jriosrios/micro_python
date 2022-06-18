from machine import Pin                 #Importamos la funcion Pin de la libreria machine
from time import sleep_ms               #Importamos la funcion sleep de la libreria time

led1 = Pin(1,Pin.OUT,value=0)
led2 = Pin(2,Pin.OUT,value=0)
led3 = Pin(3,Pin.OUT,value=0)
led4 = Pin(4,Pin.OUT,value=0)

while True:
    led1.on()
    sleep_ms(250)
    led1.off()
    
    led2.on()
    sleep_ms(250)
    led2.off()
    
    led3.on()
    sleep_ms(250)
    led3.off()
    
    led4.on()
    sleep_ms(250)
    led4.off()
