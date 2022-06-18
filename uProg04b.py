from machine import Pin                 #Importamos la funcion Pin de la libreria machine
from time import sleep_ms               #Importamos la funcion sleep_ms de la libreria time

led1 = Pin(1,Pin.OUT,value=0)           #Asignamos el Pin GP1 como salida para el led 1
led2 = Pin(2,Pin.OUT,value=0)           #Asignamos el Pin GP2 como salida para el led 2
led3 = Pin(3,Pin.OUT,value=0)           #Asignamos el Pin GP3 como salida para el led 3
led4 = Pin(4,Pin.OUT,value=0)           #Asignamos el Pin GP4 como salida para el led 4

def leds(bits,tiempo):                  #Definimos la funcion leds para que haga el proceso de encendido de leds
    led1.value((bits & 1)!=0)           #Se le asigna un valor led1 dependiendo si se cumple la condicion
    led2.value((bits & 2)!=0)           #Se le asigna un valor led2 dependiendo si se cumple la condicion
    led3.value((bits & 4)!=0)           #Se le asigna un valor led3 dependiendo si se cumple la condicion
    led4.value((bits & 8)!=0)           #Se le asigna un valor led4 dependiendo si se cumple la condicion
    sleep_ms(tiempo)                    #Esperamos en milisegundos el tiempo que se indique

while True:                             #Creamos un ciclo infinito
    leds(1,250)                         #Le damos valores a la funcion leds para que ejecute la funcion
    leds(2,250)                         #Le damos valores a la funcion leds para que ejecute la funcion
    leds(4,250)                         #Le damos valores a la funcion leds para que ejecute la funcion
    leds(8,250)                         #Le damos valores a la funcion leds para que ejecute la funcion
    leds(4,250)                         #Le damos valores a la funcion leds para que ejecute la funcion
    leds(2,250)                         #Le damos valores a la funcion leds para que ejecute la funcion
    leds(1,250)                         #Le damos valores a la funcion leds para que ejecute la funcion