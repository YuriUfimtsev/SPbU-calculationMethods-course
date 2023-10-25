from math import exp
from task_2_export_functions import Lagrange, get_interpolation_table, print_interpolation_table, \
    sort_interpolation_table
from task_2_newton_interpolator import NewtonInterpolator

print('Задача обратного интерполирования')
print('Вариант 9')


def f(x_):
    return exp(7.5 * x_)


points_count = int(input('Введите число узлов интерполяции: m + 1 = '))
a = float(input('A = '))
b = float(input('B = '))
n = int(input(f'Введите степень интерполяционного многочлена не более {points_count - 1}: n = '))

h = (b - a) / (points_count - 1)
xy = get_interpolation_table(a, h, points_count, f)
print_interpolation_table(xy)

yx = list(map(lambda p: (p[1], p[0]), xy))  # таблица для f^-1

print('Таблица значений для функции f^-1: ')
print_interpolation_table(yx)
F = float(input('F = '))
yx = sort_interpolation_table(yx, F)
print('Отсортированная таблица значений для функции f^-1: ')
print_interpolation_table(yx)

approximated_value = Lagrange(n, yx, F)
print(f'x* = {approximated_value}')
print(f'Невязка r(x*) = {abs(f(approximated_value) - F)}')
