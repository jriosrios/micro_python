from os import urandom #Importamos la libreria qu egenera un numero random
from machine import Pin,PWM #importamos la funcion Pin y PWM de machine
from time import sleep_ms #Importamos la funcion sleep_ms de time
from lib import Boton #importamos nuestra funcion boton

#Declaramos los pines de salida de los leds en una tabla
leds =[Pin(11, Pin.OUT, value=0),
       Pin(12, Pin.OUT, value=0),
       Pin(13, Pin.OUT, value=0),
       Pin(14, Pin.OUT, value=0),]

#declaramos el pin de salida del buzzer
buzzer = Pin(5, Pin.OUT, value=0)

pwmBuzzer = PWM(buzzer)
# Declaramos las los botones en una tabla
botones = [
    Boton(8),
    Boton(9),
    Boton(7),
    Boton(6)]

#Definimos las frecuencias del buzzer para cada boton 
sonido =[262,294,330,349]

def salida(num):
    pwmBuzzer.freq(sonido[num])#Establece la frecuencia al buzzer
    pwmBuzzer.duty_u16(30000)#Volumen del buzzer
    leds[num].on()#Enciende el led
    sleep_ms(500)#Pausa de 500ms para seguir con la siguiente instrucción
    leds[num].off()#Apaga el led
    pwmBuzzer.duty_u16(0)#volumen del buzzer apagado
    sleep_ms(150)

def entrada():
    tecla = -1#variable que nos servira para una condicion
    while True: #ciclo infinito
        for i in range(4):#ciclo for que va de 0 a 3
            if botones[i].actualiza():#ciclo para detemrinar si hubo modificacion en el boton
                tecla = i #se le asigna a la variable tecla el boton precionado
        if tecla!=-1:
            break# detiene le ciclo
    return tecla #retorna ewl valor de la tecla

#funcion para cunado el usuario pierda
def gameover():
    for led in leds:
        led.on()
    pwmBuzzer.freq(220)
    pwmBuzzer.duty_u16(30000)
    sleep_ms(1000)
    for led in leds:
        led.off()
    pwmBuzzer.duty_u16(0)
    sleep_ms(500)

#se declara una lista vacia
secuencia = []

while True:
    num = ord(urandom(1))%4 # se le asiga a la operacion el residuo
    secuencia.append(num) # se le añade el valor random a la secuencia
    for i in secuencia:
        salida(i)# encienden los leds correspondientes a la secuencia
    for i in secuencia:
        if(entrada()==i):#condicion si el usuario responde correctamente
            salida(i) # se llama  la funcion de salida
        else:
            secuencia = [] # se inicializa la secuencia vacia
            gameover() # se llama a la funcion de derrota
            break
            
    sleep_ms(500)