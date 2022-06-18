# Programa 13 -- Generador con OSciloscopio

# Generadpr --> Cuadrada, Diente sierra, Triangular y Senoidal
# Leds indicadores --> 12, 13, 14 y 15
# Señal PWM --> 11

from machine import Pin, PWM, Timer, ADC
from time import sleep_us
from lib import Boton

signal = Pin(11, Pin.OUT, value=0)
# Creamos el PWM y conectamos al led
pwm_signal = PWM(signal)
pwm_signal.freq(10000)

indice = 0

diente_sierra = [    0,  4000,  8000, 12000,
                 16000, 20000, 24000, 28000,
                 32000, 36000, 40000, 44000,
                 48000, 52000, 56000, 60000]
                 
cuadrada = [    0,     0,     0,     0,
                0,     0,     0,     0,
            65535, 65535, 65535, 65535,
            65535, 65535, 65535, 65535]

triangular = [    0,  8191, 16382, 24573,
              32764, 40955, 49146, 57337,
              65528, 57337, 49139, 40941,
              32743, 24545, 16347,  8149]

senoidal = [32767, 45307, 55937, 63040,
            65535, 63040, 55937, 45307,
            32767, 20227,  9597,  2494,
                0, 2494,   9597, 20227]

# El selector es para seleccionar que tabla se usara
sel = 0
# Utilizamos una tabla con las tablas para acceder mas facil
tablas = [cuadrada, diente_sierra, triangular, senoidal]
# Activar los leds que indican la onda seleccionada
led0 = Pin(12, Pin.OUT, value=1) # Onda cuadrada
led1 = Pin(13, Pin.OUT, value=0) # Onda diente sierra
led2 = Pin(14, Pin.OUT, value=0) # Onda triangular
led3 = Pin(15, Pin.OUT, value=0) # Onda senoidal

btn_sel = Boton(16)

# ADC, convertidor analogo digital
canalADC0 = ADC(0)

lookup_table = tablas[sel]

def cambia_pwm(self):
    global indice, lookup_table
    
    if indice >= len(lookup_table):
        indice = 0
        
    pwm_signal.duty_u16(lookup_table[indice])
    indice = indice + 1
    
# Modificar el periodo para modificar la amplitud
Timer(mode=Timer.PERIODIC, period=1, callback=cambia_pwm)
    
###########################################################
contador=0
while True:
    if btn_sel.actualiza():
        sel = sel + 1
        if sel > 3:
            sel = 0
        lookup_table = tablas[sel]
        
        led0.value(sel==0)
        led1.value(sel==1)
        led2.value(sel==2)
        led3.value(sel==3)
        
    if contador<100:
        lectura= canalADC0.read_u16()
        voltaje = 3.3/65520*lectura
        print(voltaje)
        
    contador += 1
    if contador>2000:
        contador = 0
    sleep_us(500)
        