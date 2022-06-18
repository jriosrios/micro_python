from machine import Pin
from time import sleep_ms

edo = 0
boton = None

def inicia(num_pin):
    global boton, edo
    boton = Pin(num_pin,Pin.IN,pull=Pin.PULL_UP)
    
def actualiza():
    global boton,edo
    
    b = boton.value()
    sal = False
    sleep_ms(10)
    
    if (b==0) and (edo==0):
        edo = 1
        sal = True
        
    if (b==1) and (edo==1):
        edo = 0
    
    return sal

inicia(16)
cuenta = 0

while True:
    if actualiza():
        cuenta = cuenta+1
        print(cuenta)
