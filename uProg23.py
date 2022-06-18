from time import time, localtime
from machine import Pin,ADC
from lib import LCD

sensor_temp = ADC(4)

led = Pin(25, Pin.OUT, value=0)
lcd = LCD(0,1,2,[3,4,5,6,7,8,9,10])

# Declaracion de variables
dias  = ['Mar','Mie','Jue','Vie','Sab','Dom','Lun']
meses = ['Ene','Feb','Mar','Abr','May','Jun','Jul',
         'Ago','Sep','Oct','Nov','Dic']

def temperatura():
    lectura = sensor_temp.read_u16()
    voltaje = 3.3/65520*lectura
    temp = 27-(voltaje-0.706)/0.001721
    return str(temp)

# Procedimiento para la fecha
def fecha(f):
    tmp = dias[f[6]]+' '
    if f[2] < 9:
        tmp = tmp + '0'
    tmp = tmp + str(f[2])+'/'
    tmp = tmp + meses[f[1]-1]+'/'
    tmp = tmp + str(f[0])+' '    
    return tmp

# Procedimiento para la hora
def hora(f):
    tmp = ''
    if f[3] < 9:
        tmp = tmp + '0'
    tmp = tmp + str(f[3])+':'
    if f[4] <= 9:
        tmp = tmp + '0'
    tmp = tmp + str(f[4])+':'
    if f[5] <= 9:
        tmp = tmp + '0'
    tmp = tmp + str(f[5])
    return tmp

seg_ant = time()
seg_ant2 = seg_ant
seg_ini = seg_ant
while True:
    seg_act = time()
    # Vemos como esta el led y encendemos/apagamos
    if seg_act >= seg_ant:
        # Cada 5 segundos realiza la accion
        seg_ant = seg_ant + 5
        
        f = localtime()
        
        file = open('datos.txt','a')
        file.write(fecha(f) + ' ' + temperatura() + '°C\n')
        file.close()
        
        #lcd.limpia()
        #lcd.textox(6,str(seg_act-seg_ini))
        led.toggle()
    
    # Imprimimos la fecha y hora
    if seg_act >= seg_ant2:
        seg_ant2 = seg_ant2 + 1
        # Guardamos la fecha en una variable
        f = localtime()

        lcd.limpia()
        lcd.cursor(0, 0)
        lcd.textox(0, fecha(f))
        lcd.textox(64, hora(f)+ ' ')
        lcd.texto(temperatura())