from machine import Pin
from time import sleep_ms
import pyRTOS #libreria de tiempo real

def led_placa(self):
    led = Pin(25,Pin.OUT,value=0)
    while True:
        led.on()
        yield[pyRTOS.timeout_ms(500)]
        led.off()
        yield[pyRTOS.timeout_ms(250)]
        
def led_externo(self):
    led = Pin(19, Pin.OUT, value=0)
    while True:
        led.on()
        yield[pyRTOS.timeout_ms(400)]
        led.off()
        yield[pyRTOS.timeout_ms(150)]

pyRTOS.add_task(pyRTOS.Task(led_placa,name='tarea1'))
pyRTOS.add_task(pyRTOS.Task(led_externo,name='tarea2'))

pyRTOS.start()