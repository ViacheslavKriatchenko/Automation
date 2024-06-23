# площадь квадрата
from math import ceil


def square(a):
    s = ceil(a * a)
    print(f'Площадь квардрата = {s}')


square(float(input('Введите любое число: ')))
