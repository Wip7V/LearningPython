import sys

numero: int = int(input('Introduce un número positivo entero: '))

if(numero < 1 ):
    print("Imposible calcular con ese número")
    sys.exit()    


def EsPrimo(numero: int) -> int:
    for j in range(2,int(numero)):
        if (int(numero) % j) == 0:
            return j
    return 0


retorno = EsPrimo(numero)

if(retorno==0):
    print("El número es primo")
else:
    print("El número no es primo, se puede dividir por: ",retorno)