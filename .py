from machine import Pin
from time import sleep_ms, sleep, time, localtime
from lib import LCD, Teclado
from dht import DHT11

# Declaracion de variables
dias  = ['Mar','Mie','Jue','Vie','Sab','Dom','Lun']
meses = ['Ene','Feb','Mar','Abr','May','Jun','Jul',
         'Ago','Sep','Oct','Nov','Dic']

pin = Pin(28, Pin.IN, Pin.PULL_UP)
dht11 = DHT11(pin,None,dht11 = True)
lcd = LCD(0,1,2,[3,4,5,6,7,8,9,10])
t = Teclado([11,12,13,14],[15,16,17,18],'123A456B789C*0#D$')
led = Pin(25,Pin.OUT,value=0)

limite = 0; periodo = 0; lim = 0; per = 0

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

def menu():
    lcd.limpia()
    lcd.textox(0,'A-Periodo')
    lcd.textox(64,'B-Limite')
    lcd.cursor(False,False)
    sleep_ms(500)
    
seg_ant = time()
seg_ant2 = seg_ant
seg_ini = seg_ant

menu()
while True:
    tecla = t.lee()

#Opcion Periodo
    if tecla =='A':
        lcd.limpia()
        lcd.texto('Periodo: ' + str(periodo))
        lcd.cursor(True,False)
        per = t.leeEntero(per,68,3,lcd)
        if (per>=1) and (per<=600):
            periodo = per
        else:
            lcd.limpia()
            lcd.texto('No valido')
            sleep_ms(500)
        menu()
#Opcion Limite        
    if tecla =='B':
        lcd.limpia()
        lcd.texto('Limite: ' + str(limite))
        lcd.cursor(True,False)
        lim = t.leeEntero(lim,68,5,lcd)
        if (lim>=1) and (lim<=10000):
            limite = lim
        else:
            lcd.limpia()
            lcd.texto('No valido')
            sleep_ms(500)
        menu()
 #Leer el .txt en la consola
        
    if t.lee() =='C':
        print(open('datos.txt').read())
        menu()
    
 #Lee temperatura       
    if tecla =='#':
        lcd.limpia()
        lcd.textox(0,'Periodo: ' + str(periodo))
        lcd.textox(64,'Limite: ' + str(limite))
        sleep_ms(500)
        
      
        while True:
            if t.lee()=='#':
                cont=0
                flag=0
                while (cont < limite) & (flag==0):
                    
                    cont = cont+1
                    f = localtime()
                    lcd.limpia()
                    T, H = dht11.read()
                    lcd.textox(128,str(cont)+' '+ 'Temp: '+ str(T)+ 'C')
                    file = open('datos.txt','a')
                    file.write(str(cont)+' '+fecha(f) +' ' + hora(f)+ ' ' + str(T) + '°C\n')
                    file.close()
                    led.on()
                    for i in range(1000):
                        sleep_ms(periodo)
                        if t.lee()=='#': #reinicia ciclo al menú principal
                            flag=1
                            break
                if flag==1:
                    led.off()
                    menu()
                flag=0
                break
                    
                if cont== limite:
                    led.off()
                    break
            if t.lee()=='*':
                        break
            
        menu()
      
