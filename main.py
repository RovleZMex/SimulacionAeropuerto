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

tiemposX = []
tiemposY = []

for i in range(n):
    tiemposX.append(ConvertirHorasAMinutos(SimularTiempo(lambdaX)))
    tiemposY.append(ConvertirHorasAMinutos(SimularTiempo(lambdaY)))

