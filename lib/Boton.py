from machine import Pin

class Boton:
    edo = 0
    boton = None

    def __init__(self, num_pin): #Self tiene estado y boton. Automaticamente se hace llamar
        self.edo = 0
        self.boton = Pin(num_pin,Pin.IN,pull=Pin.PULL_UP)
        
    def actualiza(self):
        
        b = self.boton.value()
        sal = False
        
        if (b==0) and (self.edo==0):
            self.edo = 1
            sal = True
            
        if (b==1) and (self.edo==1):
            self.edo = 0
        
        return sal