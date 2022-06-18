#PROGRAMA 6
def fun_suma(a,b):
    print(a+b)

def fun_resta(a,b):
    print(a-b)
    
def fun_nula(a,b):
    print('')
    
def fun_suma(a,b):
    print(a+b)    

funciones = [fun_suma,fun_resta,fun_nula]

for funcion in funciones:
    funcion(2,2) 