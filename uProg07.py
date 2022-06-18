#PROGRAMA 7
from machine import Pin            # Importamos la funcion Pin de la libreria machine.
from time import sleep             # Importamos la funcion sleep.

led1 = Pin(15,Pin.OUT,value = 1)   # Definimos el pin 12 como salida.
led2 = Pin(14,Pin.OUT,value = 1)   # Definimos el pin 13 como salida.

t = 0                              # Iniciamos a la variable que usaremos como contador.
v1 = 1                             # Creamos una variable para el valor que tendran la salida del led1.
v2 = 1                             # Creamos una variable para el valor que tendran la salida del led2.

while True:                        # Creamos un ciclo infinito.
    sleep(1)                       # Esperamos un segundo para la siguiente instruccion.
    t = t + 1                      # Le aumentamos un valor al contador.
    
    if(t % 2) == 0:                # Ponemos una condicion para los multiplos de 2.
        v1 = not v1                # Invertimos el valor de la salida.
        led1.value(v1)             # Le damos el valor de v2 a la salida.
        
    if(t % 3) == 0:                # Ponemos una condicion para los multiplos de 2.
        v2 = not v2                # Invertimos el valor de la salida.
        led2.value(v2)             # Le damos el valor de v2 a la salida.