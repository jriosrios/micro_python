#programa #5a--------Timer mejorado
from machine import Pin
from time import sleep_ms

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

while True:
    sel = a.value() #se guarda el valor de a
    timer = b.value() #si se presiona se guardan
    
    if (Edo==0) and (sel==0): #estado 1 y tiempo igual a 6
        led1.on() #secuencia de las luces
        led2.on()
        led3.off()
        t = 6
        Edo = 1
        sel = 1
        sleep_ms(250)
        
    if (Edo==1) and (sel==0):
        led1.off() #secuencia de las luces
        led2.on()
        led3.off()
        t = 9
        Edo = 2
        sel = 1
        sleep_ms(250)
    
    if (Edo==2) and (sel==0):
        led1.off() #secuencia de las luces
        led2.on()
        led3.on()
        t = 12
        Edo = 3
        sel = 1
        sleep_ms(250)
        
    if (Edo==3) and (sel==0):
        led1.off() #secuencia de las luces
        led2.off()
        led3.on()
        t = 15
        Edo = 4
        sel = 1
        sleep_ms(250)
        
    if (Edo==4) and (sel==0):
        led1.on() #secuencia de las luces
        led2.off()
        led3.off()
        t = 3
        Edo = 0
        sel = 1
        sleep_ms(250)
        
    if (timer==0):
        on_off.on()
        sleep_ms(t*1000) #convertirlo a segundos
        on_off.off()
        
        #Devolvera el estado 0
        led1.on()
        led2.off()
        led3.off()
        t = 3
        Edo = 0