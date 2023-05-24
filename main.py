from utensilios import *

lambdaX = random.randint(1, 6)  # Promedio de aviones que aterrizan / hora
lambdaY = random.randint(1, 5)  # Promedio de aviones que despegan / hora

lambdaZ = lambdaX - lambdaY

print("Lambda x = " + str(lambdaX))
print("Lambda y = " + str(lambdaY))
print("Lambda z = " + str(lambdaZ))

z0 = random.randint(0, 5)  # Numero de aviones en tierra en t0
print(z0)
n = int(input("Cuantas horas desea simular? "))

tiemposX = LlenarTiempos(lambdaX, n)
tiemposY = LlenarTiempos(lambdaY, n)

aterrizaje = []

sumaActual = 0
numAterrizajes = 0
for tiempo in tiemposX:
    sumaActual = sumaActual + tiempo
    if sumaActual > 60:
        sumaActual = 0
        aterrizaje.append(numAterrizajes)
        numAterrizajes = numAterrizajes + 1
    else:
        numAterrizajes = numAterrizajes + 1
aterrizaje.append(numAterrizajes)
print(aterrizaje)
print(tiemposX)
# print(len(tiemposY))
