import random
import math


def SimularTiempo(lamb):
    r = random.uniform(0, 1)
    return -math.log(1 - r, 10) / lamb


def ConvertirHorasAMinutos(hrs):
    return round(hrs * 60, 2)
