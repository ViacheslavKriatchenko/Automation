# площадь квадрата
from math import ceil

def square(a):
    s = a * a
    print(f'Площадь квардрата = {s}')

square(ceil(float(input(f'Введите любое число: '))))