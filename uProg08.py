# Importamos las funciones de las librerias
from machine import Pin, Timer
from time import sleep_ms

# Pines leds (13, 14 y 15)
led1 = Pin(15, Pin.OUT, value=1)
led2 = Pin(14, Pin.OUT, value=0)
led3 = Pin(13, Pin.OUT, value=0)
 
# Pines botones (16, 17 y 18)
a = Pin(16, Pin.IN, pull=Pin.PULL_UP)
b = Pin(17, Pin.IN, pull=Pin.PULL_UP)
c = Pin(18, Pin.IN, pull=Pin.PULL_UP)

# Definimos las funciones cb para cada led
def cb_led1(t):
    led1.off()
    
def cb_led2(t):
    led2.off()

def cb_led3(t):
    led3.off()
 
while True:
    sel1 = a.value()
    sel2 = b.value()
    sel3 = c.value()
    
    if (sel1 == 0):
        led1.on()
        temp_1 = Timer(mode=Timer.ONE_SHOT, period=3000, callback=cb_led1)
        sleep_ms(250)
    if (sel2 == 0):
        led2.on()
        temp_2 = Timer(mode=Timer.ONE_SHOT, period=6000, callback=cb_led2)
        sleep_ms(250)
    if (sel3 == 0):
        led3.on()
        temp_3 = Timer(mode=Timer.ONE_SHOT, period=9000, callback=cb_led3)
        sleep_ms(250)