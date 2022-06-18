#PROGRAMA 7
from machine import Pin                  # Importamos la funcion Pin de la libreria machine.
from time import sleep                   # Importamos la funcion sleep.

led1 = Pin(12,Pin.OUT,value = 1)         # Definimos el pin 12 como salida.
led2 = Pin(13,Pin.OUT,value = 1)         # Definimos el pin 13 como salida.

t = 0                                    # Iniciamos a la variable que usaremos como contador.

while True:                              # Creamos un ciclo infinito.
    t = t + 1                            # Le aumentamos un valor al contador.
    sleep(1)                             # Esperamos un segundo para la siguiente instruccion.
    
    if(t%2) == 0:                        # Ponemos una condicion para los multiplos de 2.
        led1.value(1 - led1.value())     # Invertimos el valor de la led1.
        
    if(t%3) == 0:                        # Ponemos una condicion para los multiplos de 2.
        led2.value(1 - led2.value())     # Invertimos el valor de la led2.