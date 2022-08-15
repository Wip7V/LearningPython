import sys

inicial = int(input("Introduce el valor inicial: "))
final = int(input("Introduce el valor final: "))

if(final<inicial):
    print("El final no puede ser mayor que el inicial")
    sys.exit()
    
numeros = []
pos = inicial


while(pos <= final):
    if( pos%2 > 0):
        numeros.append(pos)
    pos+=1

print(numeros)