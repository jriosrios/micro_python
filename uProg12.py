from machine import Pin, PWN, Timer

led= Pin(25,Pin.OUT,value=0)

pwm_led= PWN(led)
pwn_led.freq(10000)

indice=0

diente_sierra= [0, 4000, 8000, 12000,
                16000,20000,24000,28000,
                32000,36000,40000,44000,
                48000,52000,56000,6000]

triangular=[0, 8191,16382,24573,
            32764,40955,49146,57337,
            65528,57337,49146,40955,
            32764,24573,16382,8191]

cuadrara= [0,0,0,0,
           0,0,0,0
           65535,65535,65535,
           65535,65535,65535]

senoidal= [32768, 45307, 55938, 63041,
           65535, 63041, 55938, 45307,
           32768, 20228, 9597, 2494,
               0, 2494, 9597, 20228]

lookup_table=senoidal

def cambia_pwm(self):
    global indice, lookup_table
    
    if indice>= len(lookup_table):
        indice=0
        
    pwn_led.duty_u16(lookup_table[indice])
    indice= indice+1
    
Timer(mode=Timer.PERIODIC,period=50, callback=cambia_pwn)