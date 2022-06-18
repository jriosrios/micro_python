from lib import LCD, Teclado
from time import sleep_ms

# Calculadora de comida
#   ** Gorditas 17
#   ** Molletes 10
#   ** Tacos    60
#   ** Boing    16

lcd = LCD(0,1,2,[3,4,5,6,7,8,9,10])
t = Teclado([11,12,13,14],[15,16,17,18],'123A456B789C*0#D$')

def menu():
    
    lcd.textox( 0, 'A-Gordi')
    lcd.textox( 8, 'B-Molle')
    lcd.textox(64, 'C-Tacos')
    lcd.textox(72, 'D-Boing')
   

    lcd.cursor(False, False)

gorditas = 0
molletes = 0
tacos = 0
boing = 0


while True:
    tecla = t.lee()
    
    if tecla=='A':
        lcd.limpia()
        lcd.texto('Gorditas: ' + str(gorditas))
        lcd.cursor(True, False)
        gorditas = t.leeEntero(gorditas,68,2,lcd)
        menu()
    
    if tecla=='B':
        lcd.limpia()
        lcd.texto('Molletes: ' + str(molletes))
        lcd.cursor(True, False)
        molletes = t.leeEntero(molletes,68,2,lcd)
        menu()
    
    if tecla=='C':
        lcd.limpia()
        lcd.texto('Tacos: ' + str(tacos))
        lcd.cursor(True, False)
        tacos = t.leeEntero(tacos,68,2,lcd)
        menu()
        
    if tecla=='D':
        lcd.limpia()
        lcd.texto('Boing: ' + str(boing))
        lcd.cursor(True, False)
        boing = t.leeEntero(boing,68,2,lcd)
        menu()
        
    if tecla=='#':
        cuenta = gorditas*17+molletes*10+tacos*60+boing*16
        lcd.limpia()
        lcd.textox(0,'G ' + str(gorditas))
        lcd.textox(4,'M ' + str(molletes))
        lcd.textox(8,'T ' + str(tacos))
        lcd.textox(12,'B ' + str(boing))
        lcd.textox(66,'Cuenta: ' + str(cuenta))
        while True:
            if t.lee()=='#':
                break
        menu()
        
    if tecla=='*':
        gorditas = 0
        molletes = 0
        tacos = 0
        boing = 0
        
        lcd.limpia()
        lcd.textox(0,'Nueva cuenta...')
        sleep_ms(2000)
        menu()
    
