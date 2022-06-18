#En programa uProg17 de carpeta en 2do. Parcial
from machine import Pin
from time import sleep_ms

class Teclado:
    fil = [] #fil = Filas
    col = [] #col = Columnas
    txt = ''
    dep = False
    
    def __init__(self,filas,columnas,simbolos,depura=False):
        for f in filas:
            self.fil.append(Pin(f,Pin.OPEN_DRAIN,value=1))
            
        for c in columnas:
            self.col.append(Pin(c,Pin.IN,Pin.PULL_UP))
        self.txt = simbolos
        self.dep = depura
        
    def lee(self):
        indice = -1
        tecla = -1
        for f in self.fil:
            f.off()
            for c in self.col:
                indice = indice + 1
                if (c.value()==0):
                    tecla = indice
                
                if self.dep:
                    if (c.value()==0):
                        print('[',self.txt[indice],']',end='')
                    else:
                        print(' ',self.txt[indice],' ',end='')
            if self.dep:
                print('')
            f.on()
        return self.txt[tecla]
    
    def leeEntero(self,num,pos,maximo,lcd): #(numero,posicion)
        numero = num
        s = ''
        lcd.mueve(pos)
        while True:
            tecla = self.lee()
            if (tecla in '0123456789') and (len(s)<maximo):
                s=s+tecla
                lcd.texto(tecla)
                sleep_ms(350)
            if tecla == '#':
                if s!='':
                    numero = int(s)
                else:
                    return num
                return numero
            if tecla == '*':
                return num