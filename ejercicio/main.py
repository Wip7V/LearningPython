import sys
from calculadora import sumar,restar,dividir,multiplicar

opcion: int = int(input("Elije una opción:\n 1) Sumar\n 2) Restar\n 3) Multiplicar\n 4) Dividir\n:"))

val1: int = int(input("Introduce el primer valor: "))
val2: int = int(input("Introduce el segundo valor: "))

if(opcion == 1):
    print("El resultado de la Suma es: ",sumar(val1,val2))
    
if(opcion == 2):
    print("El resultado de la Resta es: ",restar(val1,val2))
    
if(opcion == 3):
    print("El resultado de Multiplicar es: ",multiplicar(val1,val2))
    
if(opcion == 4):
    if(val1 == 0 or val2 ==0):
        print("División con 0 da error")
        sys.exit()  
    print("El resultado de Dividir es: ",dividir(val1,val2))


