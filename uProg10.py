from machine import Pin
from time import sleep_ms

# Pines botones (16, 17 y 18)
btn1 = Pin(16, Pin.IN, pull=Pin.PULL_UP)
btn2 = Pin(17, Pin.IN, pull=Pin.PULL_UP)

cont = 0

while True:
    plus = btn1.value()
    rst = btn2.value()
    
    if (plus == 0):
        cont = cont+1
        print(cont)
        
    if (rst == 0):
        cont = 0
        sleep_ms(150)
        print(cont)