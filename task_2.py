import polynomial as pol
from math import exp


def f(x):
    return 1 - exp(-x) + x ** 2


print('Задача алгебраического интерполирования')
print('Вариант 9')

points_count = int(input('Введите количество узлов интерполяции: m + l = '))
print('Введите отрезок, на котором нужно интерполировать функцию: ')
A = float(input('A = '))
B = float(input('B = '))
x = [A + i * (B - A) / points_count for i in range(points_count)] # узлы интерполяции
y = [f(x[i]) for i in range(points_count)]
print('Таблица значений функции: ')
for j in range(points_count):
    print(f'f(x{j}) = {y[j]}')

x0 = float(input('Введите точку интерполирования: x = '))
n = int(input('Введите степень интерполяционного многочлена: n = '))




