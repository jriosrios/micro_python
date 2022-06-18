#Implementación de Pantalla LCD.

from machine import Pin
from time import sleep_ms, sleep_us

#Declaramos las señales
RS = Pin(0,Pin.OUT,value=0)
RW = Pin(1,Pin.OUT,value=0)
E  = Pin(2,Pin.OUT,value=0)

D0 = Pin(3,Pin.OUT,value=0)
D1 = Pin(4,Pin.OUT,value=0)
D2 = Pin(5,Pin.OUT,value=0)
D3 = Pin(6,Pin.OUT,value=0)
D4 = Pin(7,Pin.OUT,value=0)
D5 = Pin(8,Pin.OUT,value=0)
D6 = Pin(9,Pin.OUT,value=0)
D7 = Pin(10,Pin.OUT,value=0)

def LCD16(_rs,_rw,datos):
    RS.value(_rs)
    RW.value(_rw)
    
    sleep_us(1)
    E.on()

    cad = bin(256+datos)
    D7.value(cad[-8]=='1')
    D6.value(cad[-7]=='1')
    D5.value(cad[-6]=='1')
    D4.value(cad[-5]=='1')
    D3.value(cad[-4]=='1')
    D2.value(cad[-3]=='1')
    D1.value(cad[-2]=='1')
    D0.value(cad[-1]=='1')

    sleep_us(1)
    E.off()
    sleep_us(37)
    

#Proceso de inicialización de la pantalla LCD16x2
sleep_ms(15) #Esperamos 15ms
LCD16(0,0,48) #Mandamos 00 0011 xxxx
sleep_us(4100) #Equivale a 4.1ms
LCD16(0,0,48) #Mandamos 00 0011 xxxx
sleep_us(100) #Esperamos 100us
LCD16(0,0,48) #Mandamos 00 0011 xxxx

LCD16(0,0,56)   # Mandamos 00 0011 NFxx
                #N=1: 2 líneas, N=0:1 linea
                #F=1: 5x10puntos, F=0: 5x8p

LCD16(0,0,8)    #Display off
LCD16(0,0,1)    #Display clear
LCD16(0,0,7)      #Mandamos 00 0000 01 I/D S
                #I/D=1: Incrementa el cursor, I/D: decrementa
                #S=1: Realiza desplazamiento, S=0 sin desplazamiento.