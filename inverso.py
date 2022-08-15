numeros = []

pos = 1
while(pos<=100):
    numeros.append(pos)
    pos+=1

numeros.sort(reverse=True)

print(numeros)