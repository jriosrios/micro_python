from machine import Pin,Timer            # Importamos la funcion Pin de la libreria machine.
from time import sleep                   # Importamos la funcion sleep.

led1 = Pin(12,Pin.OUT,value = 1)         # Definimos el pin 12 como salida.
led2 = Pin(13,Pin.OUT,value = 1)         # Definimos el pin 13 como salida.

def cb_led1(t):
    led1.value(1 - led1.value())
    
def cb_led2(t):
    led2.value(1 - led2.value())
    
temporizador_1 = Timer(mode=Timer.PERIODIC, period = 2000, callback = cb_led1)
temporizador_2 = Timer(mode=Timer.PERIODIC, period = 3000, callback = cb_led2)