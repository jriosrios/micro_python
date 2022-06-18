from machine import Pin
from time import sleep_ms, sleep_us

#Declaramos las señales
class LCD:
    RS=None
    RW=None
    E=None
    D0=None
    D1=None
    D2=None
    D3=None
    D4=None
    D5=None
    D6=None
    D7=None
    
    def __init__(self,rs,rw,w,d):
        self.RS = Pin(rs,Pin.OUT,value=0)
        self.RW = Pin(rw,Pin.OUT,value=0)
        self.E  = Pin(w,Pin.OUT,value=0)

        self.D0 = Pin(d[0],Pin.OUT,value=0)
        self.D1 = Pin(d[1],Pin.OUT,value=0)
        self.D2 = Pin(d[2],Pin.OUT,value=0)
        self.D3 = Pin(d[3],Pin.OUT,value=0)
        self.D4 = Pin(d[4],Pin.OUT,value=0)
        self.D5 = Pin(d[5],Pin.OUT,value=0)
        self.D6 = Pin(d[6],Pin.OUT,value=0)
        self.D7 = Pin(d[7],Pin.OUT,value=0)
        self.__inicia__()

    def LCD16(self,_rs,_rw,datos):
        self.RS.value(_rs)
        self.RW.value(_rw)
        
        sleep_us(1)
        self.E.on()
        cad = bin(256+datos)
        
        self.D7.value(cad[-8]=='1')
        self.D6.value(cad[-7]=='1')
        self.D5.value(cad[-6]=='1')
        self.D4.value(cad[-5]=='1')
        self.D3.value(cad[-4]=='1')
        self.D2.value(cad[-3]=='1')
        self.D1.value(cad[-2]=='1')
        self.D0.value(cad[-1]=='1')

        sleep_us(1)
        self.E.off()
        sleep_us(37)
    
    def texto(self,texto):
        for letra in texto:
            self.LCD16(1,0,ord(letra))

    def textox(self,x,t):
        self.LCD16(0,0,128+x)
        self.texto(t)
        
    def __inicia__(self):   
        sleep_ms(15) 
        self.LCD16(0,0,48) 
        sleep_us(4100) 
        self.LCD16(0,0,48) 
        sleep_us(100) 
        self.LCD16(0,0,48)
        self.LCD16(0,0,56)     
                       
        self.LCD16(0,0,8)   
        self.LCD16(0,0,1)    
        self.LCD16(0,0,7)

        self.LCD16(0,0,15)
        self.LCD16(0,0,15)
        self.LCD16(0,0,6)
        
    def limpia(self):
        self.LCD16(0,0,1)
    
    def cursor(self,visible,parpadeo):
        cmd = 12
        if visible:
            cmd = cmd +2
        if parpadeo:
            cmd = cmd +1
        self.LCD16(0,0,cmd)
    
    def mueve(self,x):
        self.LCD16(0,0,128+x)