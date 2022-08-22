from pickle import *

class Vehiculo:
    color: str
    ruedas: int
    pertas: int

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color: "+self.color+ ", Ruedas: "+str(self.ruedas)+", Puertas: "+str(self.puertas)

coche = Vehiculo("Negro", "4", "5")
print(coche)

archivo = open('coche', 'w+b')
dump(coche, archivo)
archivo.close()

archivo = open('coche', 'r+b')
coche = load(archivo)
archivo.close()

print(coche)
