from machine import Pin                 #Importamos la funcion Pin de la libreria machine
from time import sleep_ms                  #Importamos la funcion sleep de la libreria time

led1 = Pin(1,Pin.OUT,value=0)
led2 = Pin(2,Pin.OUT,value=0)
led3 = Pin(3,Pin.OUT,value=0)
led4 = Pin(4,Pin.OUT,value=0)

def leds(d1,d2,d3,d4,tiempo):
    led1.value(d1)
    led2.value(d2)
    led3.value(d3)
    led4.value(d4)
    sleep_ms(tiempo)

while True:
    leds(1,0,0,0,250)
    leds(0,1,0,0,250)
    leds(0,0,1,0,250)
    leds(0,0,0,1,250)
    leds(0,0,1,0,250)
    leds(0,1,0,0,250)
    leds(1,0,0,0,250)
