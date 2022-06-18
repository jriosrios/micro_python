from machine import Pin                 #Importamos la funcion Pin de la libreria machine.
from time import sleep                  #Importamos la funcion sleep de la libreria time.

led = Pin(16,Pin.OUT,value=0)            #Asignamos al pin 2 como salida inicializandolo en 0 (apagado).
boton = Pin(15,Pin.IN,Pin.PULL_DOWN)     #Activo en alto (Pull-Down).

while True:
    if boton.value()==1:                #Hacemos una condicion para que se ejecute cuando el boton este en 1.
        led.on()                        #Encendemos el led.
        sleep(3)                        #Esperamos 3 segundos para seguir con la siguiente instrucción.
        led.off()                       #Apagamos el led.
    
            
