from time import sleep_ms       #Importamos de la libreria time la funcion sleep_ms
from machine import Pin         #Importamos de la libreria machine la funcion Pin

led = Pin(25,Pin.OUT,value = 0) #Asignamos a la variable led un pin del Microcontrolador

while True:                     #Creamos un ciclo Infinito
    led.on()                    #Encendemos el led
    sleep_ms(1000)              #Esperamos 1000 milisegundos para dar la siguiente instruccion
    led.off()                   #Apagamos el led
    sleep_ms(1000)              #Esperamos 1000 milisegundos para dar la siguiente instruccion

