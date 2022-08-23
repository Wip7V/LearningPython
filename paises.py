paises = input("Escribe un listado de paises separados por comas: \n")

paises = paises.split(",")
paises = set(paises)
paises = sorted(paises)
lista = ",".join(paises)

print("\nResultado")
print(lista)
