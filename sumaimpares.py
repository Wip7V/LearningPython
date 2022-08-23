from functools import reduce

def sumaimpares(nums):
    impares = list(filter(lambda p : p%2 != 0, nums))
    res = reduce(lambda x, y: x+y, impares)
    return res


numeros = [1,2,3,4,5,6]

print("Los numero son: ",numeros)

sumaimpares(numeros)
print("Y la suma de solo los elementos impares es: ",sumaimpares(numeros))
