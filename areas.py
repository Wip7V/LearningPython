
def AreaCirculo(radio: float) -> float:
    return (3.1416*(radio*radio))
    
def AreaTriangulo(base: float, altura: float,) -> float:
    return ((altura*base)/2)
    
    
opcion: int = int(input("Pulsa 1 para Área del Triangulo o pulsa 2 para Área del Circulo "))

if(opcion==1):
    base: float = float(input("La base del triangulo: "))
    altura: float = float(input("La altura del triangulo: "))
    print("Área del triangulo es ",AreaTriangulo(base,altura))
else:
    radio: float = float(input("El radio del circulo: "))
    print("Área del circulo es ",AreaCirculo(radio))
