from machine import Pin
from time import sleep_ms

class Teclado:
    fil = []
    col = []
    txt = []
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
            
            
                
            f.on()
            if self.dep:
                print('')
                sleep(250)
                
        return self.txt[tecla]

        
t = Teclado([11,12,13,14],[15,16,17,18],'123A456B789C*0#D-',False)

while True:
    print('La tecla es:',t.lee())
    sleep_ms(200)




