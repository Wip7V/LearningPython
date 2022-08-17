import sys

year: int = int(input("Introduce el año: "))

if(year < 1 ):
    print("Imposible calcular con ese número")
    sys.exit()


def bisiesto(year: int) -> bool:
    if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return True
    else:
        return False

if(bisiesto(year)):
    print("Es bisiesto")
else:
    print("No es bisiesto")