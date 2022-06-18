#programa #5c--------Timer mejorado
from machine import Pin
from time import sleep_ms
from time import sleep

#Entradas
a = Pin(16, Pin.IN,pull=Pin.PULL_UP) #botones
b = Pin(17, Pin.IN,pull=Pin.PULL_UP)

#Salidas
led1 = Pin(12,Pin.OUT,value=1) #indicar que el sistema esta encendido
led2 = Pin(13,Pin.OUT,value=0)
led3 = Pin(14,Pin.OUT,value=0)
on_off = Pin(15,Pin.OUT,value=0)

Edo = 0
t = 3

def fsm(ld1,ld2,ld3,tiempo,edo2):
    global t, Edo,sel
    led1.value(ld1)
    led2.value(ld2)
    led3.value(ld3)
    t=tiempo
    Edo=edo2
    sel=1
    sleep_ms(250)

tabla_led1 = [1,0,0,0,1]
tabla_led2 = [1,1,1,0,0]
tabla_led3 = [0,0,1,1,0]
tabla_t = [6,9,12,15,3]
tabla_Edo = [1,2,3,4,0]

while True:
    sel = a.value() 
    timer = b.value() 
    
    if(sel==0):
        led1.value(tabla_led1[Edo])
        led2.value(tabla_led2[Edo])
        led3.value(tabla_led3[Edo])
        t = tabla_t[Edo]
        Edo = tabla_Edo[Edo]
        sleep_ms(250)
    
    if (timer==0):
        on_off.on()
        sleep(t)
        on_off.off()
        fsm(1,0,0,3,0)
        led1.on()
        led2.off()
        led3.off()
        t=3
        Edo=0