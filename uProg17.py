#Implementación de Pantalla LCD.

from machine import Pin
from time import sleep_ms, sleep_us
from lib import LCD

lcd = LCD(0,1,2,[3,4,5,6,7,8,9,10])
lcd.cursor(False,False)

lcd.textox(128,'Hola: Indalecio')
lcd.textox(64,'Rios Rios')
sleep_ms(2000)
lcd.limpia()
sleep_ms(2000)

lcd.cursor(False,False)

lcd.texto("Numero:")
for i in range(1,21):
    lcd.textox(8,str(i))
    sleep_ms(250)

lcd.textox(68,"[    ]")
lcd.cursor(True,False)
while True:
    for i in range(69,73):
        lcd.mueve(i)
        sleep_ms(200)
        
#Subtitulos
# lcd.textox(128,'Digamos')
# sleep_ms(2000)
# lcd.textox(64,'Que te creo')
# sleep_ms(2500)
# lcd.textox(20,'Que te arrepientes')
# sleep_ms(3000)
# lcd.textox(84,'Pero es diferente')
# sleep_ms(2500)
# lcd. limpia()
# lcd.textox(128,'A que te perdone')
# sleep_ms(2500)
# lcd.textox(64,'Sere buena gente')
# sleep_ms(2500)
# lcd.textox(20,'Pero no tu pendejo')
# sleep_ms(3000) 
# lcd.textox(84,'Yo no me dejo')




