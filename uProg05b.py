#PROGRAMA 5B TIMER CON FUNCION
from machine import Pin                      #Importamos la funcion Pin de la libreria machine
from time import sleep_ms                    #Importamos la funcion sleep_ms

a = Pin(16, Pin.IN, pull=Pin.PULL_UP)        #Definimos el pin 16 como entrada
b = Pin(17, Pin.IN, pull=Pin.PULL_UP)        #Definimos el pin 17 como entrada

led1 = Pin(12,Pin.OUT,value=1)               #Definimos el pin 12 como salida
led2 = Pin(13,Pin.OUT,value=0)               #Definimos el pin 13 como salida
led3 = Pin(14,Pin.OUT,value=0)               #Definimos el pin 14 como salida
on_off = Pin(15,Pin.OUT,value=0)             #Definimos el pin 15 como salida

edo = 0                                      #Se inicializa el estado en 0
t = 3                                        #Se inicializa el tiempo en 3

def fsm(L1,L2,L3,tiempo,edo2):               #Iniciamos una funcion para la maquina de estados
    global t,edo,sel                         # Declaramos como variabkes globales para que se puedan modificar fuera de la funcion
    
    led1.value(L1)                           #Se le asigna a la salida del led1 el valor de L1
    led2.value(L2)                           #Se le asigna a la salida del led2 el valor de L2
    led3.value(L3)                           #Se le asigna a la salida del led3 el valor de L3
    t=tiempo                                 #Se le asigna al valor de t el valor de tiempo
    edo = edo2                               #Se le asigna al valor de edo el calor de edo2
    sel = 1                                  #Se inicializa al selector en 1 para que no vuelva a entrar en el if inmediatamente
    sleep_ms(250)                            #Esperamos 250 milisegundos para la siguiente instruccion

while True:                                  #Se crea un ciclo infinito
    sel = a.value()                          #Se inicializa el valor de sel a lo que se tenga en la entrada a
    timer = b.value()                        #Se inicializa el valor del timer a lo que se tenga en la entrada b
    
    if (edo==0) and (sel==0):                #Se pone la condicion para que entre en el estado 1
        fsm(1,1,0,6,1)                       #Se le dan valores a la funcion para que se ejecute
        
    if (edo==1) and (sel==0):                #Se pone la condicion para que entre en el estado 2
        fsm(0,1,0,9,2)                       #Se le dan valores a la funcion para que se ejecute
    
    if (edo==2) and (sel==0):                #Se pone la condicion para que entre en el estado 3
        fsm(0,1,1,12,3)                      #Se le dan valores a la funcion para que se ejecute
    
    if (edo==3) and (sel==0):                #Se pone la condicion para que entre en el estado 4
        fsm(0,0,1,15,4)                      #Se le dan valores a la funcion para que se ejecute
       
    if (edo==4) and (sel==0):                #Se pone la condicion para que entre en el estado 5
        fsm(1,0,0,3,0)                       #Se le dan valores a la funcion para que se ejecute
    
    if (timer==0):                           #Se pone la condicion para el estado de encendido apagado
        on_off.on()                          #Se enciende el led de encendido apagado
        sleep_ms(t*1000)                     #Esperamos el tiempo en segundos
        on_off.off()                         #Se apaga el led de encendido apagado
        
        fsm(1,0,0,3,0)                       #Se incializa al estado 1