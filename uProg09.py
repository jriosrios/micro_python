from machine import Pin, Timer   #Importamos las fucniones Pin y Timer de la libreria machine
from time import sleep_ms        #Importamos la funcion sleep_ms de la libreria time

# Pines leds (13, 14 y 15)
led1 = Pin(15, Pin.OUT, value=0)  #Asignamos a la variable led1 el pin de salida 15 inicializado en 0
led2 = Pin(14, Pin.OUT, value=0)  #Asignamos a la variable led2 el pin de salida 14 inicializado en 0
led3 = Pin(13, Pin.OUT, value=0)  #Asignamos a la variable led3 el pin de salida 13 inicializado en 0
 
# Pines botones (16, 17 y 18)
btn1 = Pin(16, Pin.IN, pull=Pin.PULL_UP)  #Asignamos a la variable btn1 el pin de entrada 16
btn2 = Pin(17, Pin.IN, pull=Pin.PULL_UP)  #Asignamos a la variable btn2 el pin de entrada 17
btn3 = Pin(18, Pin.IN, pull=Pin.PULL_UP)  #Asignamos a la variable btn3 el pin de entrada 18

temp1 = None #Se crea una variable sin valor
temp2 = None #Se crea una variable sin valor
temp3 = None #Se crea una variable sin valor

def cb_led1(t):  
    global temp1     #declaramos nuestra variable global
    led1.off()       #apagamos el led1
    temp1.deinit()   #Apagamos el timer
    temp1 = None     #Volvemos a la variable none de que no hay timer encendido

def cb_led2(t):
    global temp2     #declaramos nuestra variable global
    led2.off()       #apagamos el led1
    temp2.deinit()   #Apagamos el timer
    temp2 = None     #Volvemos a la variable none de que no hay timer encendido

def cb_led3(t):
    global temp3     #declaramos nuestra variable global
    led3.off()       #apagamos el led1
    temp3.deinit()   #Apagamos el timer
    temp3 = None     #Volvemos a la variable none de que no hay timer encendido

while True:             #Creamos el siclo infinito
    sw1 = btn1.value()  #asignamos a la variable bw1
    sw2 = btn2.value()  #asignamos a la variable bw2
    sw3 = btn3.value()  #asignamos a la variable bw3
    
    if(sw1 == 0):            #Condicion para detectar un valor en la entrada
        if temp1 is None:    #condicion para verificar el valor de temp1
            led1.on()        #Enciende el Led 1
            temp1 = Timer(mode=Timer.ONE_SHOT, period=5000, callback=cb_led1) # a la variable se le asigna la funcion timer con el modo de operacion del temporalizador
        else:                #Si no se cumple la condicion ejecuta otras instrucciones   
            led1.off()       #apaga el led 1
            temp1.deinit()   #Apaga el temporalizador1
            temp1 = None     #Se limpia el valor de la variable
        sleep_ms(250)        #esperamos 250 miliseguntos para continuar con la siguiente instruccion
        
    if(sw2 == 0):            #Condicion para detectar un valor en la entrada
        if temp2 is None:    #condicion para verificar el valor de temp1
            led2.on()        #Enciende el Led 2
            temp2 = Timer(mode=Timer.ONE_SHOT, period=5000, callback=cb_led2) # a la variable se le asigna la funcion timer con el modo de operacion del temporalizador
        else:                #Si no se cumple la condicion ejecuta otras instrucciones
            led2.off()       #apaga el led 2
            temp2.deinit()   #Apaga el temporalizador2
            temp2 = None     #Se limpia el valor de la variable
        sleep_ms(250)        #esperamos 250 miliseguntos para continuar con la siguiente instruccion
    
    if(sw3 == 0):            #Condicion para detectar un valor en la entrada
        if temp3 is None:    #condicion para verificar el valor de temp1
            led3.on()        #Enciende el Led 3
            temp3 = Timer(mode=Timer.ONE_SHOT, period=5000, callback=cb_led3) # a la variable se le asigna la funcion timer con el modo de operacion del temporalizador
        else:                #Si no se cumple la condicion ejecuta otras instrucciones
            led3.off()       #apaga el led 3
            temp3.deinit()   #Apaga el temporalizador3
            temp3 = None     #Se limpia el valor de la variable
        sleep_ms(250)        #esperamos 250 miliseguntos para continuar con la siguiente instruccion