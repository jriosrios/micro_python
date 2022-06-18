from machine import Pin
from time import ticks_ms

led1 = Pin(12,Pin.OUT,value = 1)
led2 = Pin(13,Pin.OUT,value = 1)

tiempo1 = 2000
tiempo2 = 3000

while True:
    if tiempo1 < ticks_ms():
        tiempo1 = tiempo1 + 2000
        led1.value(1 - led1.value())

    if tiempo2 < ticks_ms():
        tiempo2 = tiempo1 + 3000
        led2.value(1 - led2.value())