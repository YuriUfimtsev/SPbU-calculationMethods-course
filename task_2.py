import polynomial as pol
from math import exp


def f(x):
    return 1 - exp(-x) + x ** 2


def product(l):
    result = 1
    for i in range(len(l)):
        result *= l[i]
    return result


def w(n, x, z):
    return product([(x - z[k]) for k in range(n + 1)])


print('Задача алгебраического интерполирования')
print('Вариант 9')

points_count = int(input('Введите количество узлов интерполяции: m + 1 = '))
print('Введите отрезок, на котором нужно интерполировать функцию: ')
A = float(input('A = '))
B = float(input('B = '))
z = [A + i * (B - A) / points_count for i in range(points_count)] # узлы интерполяции
y = [f(z[i]) for i in range(points_count)]
print('Таблица значений функции: ')
for j in range(points_count):
    print(f'f({z[j]}) = {y[j]}')

x = float(input('Введите точку интерполирования: x = '))
n = int(input(f'Введите степень интерполяционного многочлена n (n < {points_count}): '))

# сортируем узлы интерполирования по расстоянию от точки x
z1 = [(abs(z[i] - x), z[i]) for i in range(points_count)]
z1.sort()
z = list(map(lambda p: p[1], z1))
y = [f(z[i]) for i in range(points_count)]
for j in range(points_count):
    print(f'f({z[j]}) = {y[j]}')











