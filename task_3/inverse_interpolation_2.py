from math import exp
from task_2_export_functions import *
from task_2_newton_interpolator import NewtonInterpolator
import polynomial


def get_roots_segments(A, B, N):
    h = (B - A) / N
    control_points = [A + i * h for i in range(0, N + 1)]
    segments = []
    for i in range(1, N + 1):
        c, d = control_points[i - 1], control_points[i]
        if f(c) * f(d) < 0:
            segments.append((c, d))
    return segments


def print_segments(segments):
    print('\nОтрезки перемены знака функции')
    for segment in segments:
        print(f'[{segment[0]}, {segment[1]}]')
    print(f'Общее количество отрезков: {len(segments)}')


def secant(segment, polynom_: polynomial.Polynomial):
    a, b = segment[0], segment[1]
    eps = 10 ** -10
    x = [a, b]
    while abs(x[-1] - x[-2]) >= eps:
        x.append(x[-1] - ((x[-1] - x[-2]) * (polynom_.calculate(x[-1]) / (polynom_.calculate(x[-1]) - polynom_.calculate(x[-2])))))
    return x[-1]


points_count = int(input('Введите число узлов интерполяции: m + 1 = '))
a = float(input('A = '))
b = float(input('B = '))

h = (b - a) / (points_count - 1)
xy = get_interpolation_table(a, h, points_count, f)
print('Таблица значений для функции f: ')
print_interpolation_table(xy)
while True:
    n = int(input(f'Введите степень интерполяционного многочлена не более {points_count - 1}: n = '))

    F = float(input('F = '))

    c = (a + b) / 2
    xy = sorted(xy, key=lambda array: abs(c - array[0]))
    print_interpolation_table(xy)
    interpolator = NewtonInterpolator()
    interpolator.reform_separated_differences_table(xy)
    interpolator.form_polynomial(n - 1)
    polynom = interpolator.polynomial

    segments = get_roots_segments(a, b, points_count)
    print_segments(segments)
    x0s = []
    for s in segments:
        x0s.append(secant(s, polynom - polynomial.Polynomial(F)))

    for x0 in x0s:
        print(f'x* = {x0}')
        print(f'Невязка r = {abs(f(x0) - F)}')

    # x0 = secant((a, b), polynom - polynomial.Polynomial(F))
    # print(f'x* = {x0}')
    # print(f'Невязка r = {abs(f(x0) - F)}')
