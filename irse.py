from datetime import datetime

ahora = datetime.today()

year = int(ahora.strftime("%Y"))
month = int(ahora.strftime("%m"))
day = int(ahora.strftime("%d"))

salida = datetime(year, month, day, 19, 00, 00)

if(ahora > salida):
    print("Ya es hora de irse")
else:
    dif = salida - ahora
    print("Aún faltan: ", str(dif).split(".")[0])

