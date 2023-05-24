import random
import math


def SimularTiempo(lamb):
    r = random.random()
    result = -math.log(1 - r, 10) / lamb
    print(result)
    return result


def ConvertirHorasAMinutos(hrs):
    return round(hrs * 60, 2)


def LlenarTiempos(lamb, hrs):
    result = []
    sumaTiempos = 0
    while sumaTiempos < hrs * 60:
        nuevoTiempo = ConvertirHorasAMinutos(SimularTiempo(lamb))
        result.append(nuevoTiempo)
        sumaTiempos = sumaTiempos + nuevoTiempo
    print(sumaTiempos)
    return result