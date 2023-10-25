from math import exp
from task_2_export_functions import *
from task_2_newton_interpolator import NewtonInterpolator
import polynomial


def f(x_):
    return exp(7.5 * x_)


def secant(segment, polynom_: polynomial.Polynomial):
    a, b = segment[0], segment[1]
    eps = 10 ** -6
    x = [a, b]
    while abs(x[-1] - x[-2]) >= eps:
        x.append(x[-1] - ((x[-1] - x[-2]) * (
                    polynom_.calculate(x[-1]) / (polynom_.calculate(x[-1]) - polynom_.calculate(x[-2])))))
    return x[-1]


points_count = int(input('Введите число узлов интерполяции: m + 1 = '))
a = float(input('A = '))
b = float(input('B = '))
n = int(input(f'Введите степень интерполяционного многочлена не более {points_count - 1}: n = '))

h = (b - a) / (points_count - 1)
xy = get_interpolation_table(a, h, points_count, f)
print('Таблица значений для функции f: ')
print_interpolation_table(xy)

F = float(input('F = '))

c = (a + b) / 2
xy = sorted(xy, key=lambda array: abs(c - array[0]))

interpolator = NewtonInterpolator()
interpolator.reform_separated_differences_table(xy)
interpolator.form_polynomial(n - 1)
polynom = interpolator.polynomial

x0 = secant((a, b), polynom - polynomial.Polynomial(F))
print(f'x* = {x0}')
print(f'Невязка r = {f(x0) - F}')
