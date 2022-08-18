
class Vehiculo():
    color: int
    ruedas: int
    pertas: int

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def getDatos(self) -> str:
        return "Color: "+self.color+ " Ruedas: "+str(self.ruedas)+" Puertas: "+str(self.puertas)
    


class Coche(Vehiculo):

    velocidad: int
    cilindrada: int

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def getDatos(self):
        return "Color: "+self.color+ " Ruedas: "+str(self.ruedas)+" Puertas: "+str(self.puertas)+" Velocidad: "+str(self.velocidad)+"km Cilindrada: "+str(self.cilindrada)+"cc"


coche = Coche("Negro", 4, 5, 40, 2000)
print(coche.getDatos())