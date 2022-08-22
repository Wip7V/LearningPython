archivo = open("texto.txt","w")
archivo.write("Hola Mundo \n")
archivo.close()


archivo = open("texto.txt","a")
archivo.write("Aquí estamos \n")
archivo.close()


archivo = open("texto.txt","r")
print(archivo.read())
archivo.close()