##Teclado 4x4
from machine import Pin
from time import sleep_ms
from lib import Teclado, LCD

lcd= LCD(0,1,2,[3,4,5,6,7,8,9,10])
t= Teclado([11,12,13,14],[15,16,17,18],'123A456B789C*0#D$')
s= ''
while True:
    tecla= t.lee()
    #simbolos numericos 0,1,2,3,4,5,6,7,8,9
    #Cantidad variable de digitos y limitada
    #    #--> aceptar numero
    #    *--> cancelar numero
    if tecla!= '$':
        if tecla in '0123456789':
            s=s+tecla
        if tecla == '#':
            numero=int(s)
            lcd.texto(64,str(numero))
        if tecla == '*':
            s= ''
            lcd.limpia()  
        lcd.texto(0,s)
        print('La tecla es ',tecla) 
        sleep_ms(250)
# 2 digitos 0 -->99
# 3 digitos 0 -->999
# 4 digitos 0 -->9999
# 5 digitos 0 -->99999
# 6 digitos 0 -->999999
# 7 digitos 0 -->9999999