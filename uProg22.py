from lib import LCD,Teclado
from time import sleep_ms

opciones = [['Texto1',100],['Texto2',200],['Texto3',300],
            ['Texto4',400],['Texto5',500],['Texto6',600],
            ['Texto7',700],['Texto8',800],['Texto9',900],
            ['Texto10',1000],['Texto11',1100]]

N = len(opciones)

lcd = LCD(0,1,2,[3,4,5,6,7,8,9,10])
t = Teclado([11,12,13,14],[15,16,17,18],'123A456B789C*0#D$')

indice = 0

def salida():
    lcd.limpia()
    lcd.textox(0,opciones[indice][0])
    lcd.textox(8,str(opciones[indice][1]))
    lcd.textox(75,str(indice+1))
    lcd.textox(77,'/'+str(N))
    
    sleep_ms(300)
               
    
salida()
while True:
    tecla = t.lee()
    if tecla == 'A':
        indice = indice - 1
        if indice<0:
            indice = N-1
        salida()
            
    if tecla == 'B':
        indice = indice + 1
        if indice>=N:
            indice = 0
        salida()
        
    if tecla == 'C':
        lcd.textox(61, '[      ]')
        opciones[indice][1]=t.leeEntero(opciones[indice][1],62,6,lcd)
        salida()
        