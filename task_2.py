import polynomial as pol
from task_2_newton_interpolator import NewtonInterpolator
from math import exp


def f(x_):
    return 1 - exp(-x_) + x_ ** 2


def Lagrange(n_, z_, x_):
    return L(n_, z_).calculate(x_)


def product(l_):
    result = pol.Polynomial(1.0)
    for i in range(len(l_)):
        result *= l_[i]
    return result


def w(n_, z_):
    return product([pol.Polynomial(1.0, -z_[k]) for k in range(n_ + 1)])


def l(k, n_, z_):
    return w(n_, z_) // (pol.Polynomial(1.0, -z_[k]) * w(n_, z_).derivative.calculate(z_[k]))


def L(n_, z_):
    result = pol.Polynomial(0.0)
    for k in range(n_ + 1):
        result += pol.Polynomial(f(z_[k])) * l(k, n_, z_)
    return result


def new_lagrange(n_, z_, x):
    result = 0
    for k in range(n_ + 1):
        p1 = 1
        for i in range(n_ + 1):
            if i != k:
                p1 *= (x - z_[i])
        p2 = 1
        for i in range(n_ + 1):
            if i != k:
                p2 *= (z_[k] - z_[i])
        result += f(z_[k]) * p1 / p2
    return result


print('Задача алгебраического интерполирования')
print('Вариант 9')

points_count = int(input('Введите количество узлов интерполяции: m + 1 = '))
print('Введите отрезок, на котором нужно интерполировать функцию: ')
A = float(input('A = '))
B = float(input('B = '))

z = [A + i * (B - A) / (points_count - 1) for i in range(points_count)]  # узлы интерполяции
y = [f(z[i]) for i in range(points_count)]
print('Таблица значений функции: ')
for j in range(points_count):
    print(f'f({z[j]}) = {y[j]}')

last_point = 0
is_program_over = False
is_first_iteration = False
newton_interpolator = NewtonInterpolator()

while not is_program_over:
    x0 = float(input('Введите точку интерполирования: x = '))
    n = int(input(f'Введите степень интерполяционного многочлена не выше {points_count - 1}: n = '))
    while n >= points_count:
        n = int(input('Введено недопустимое значение. Введите степень интерполяционного многочлена не выше '
                      f'{points_count - 1}: n = '))

    # сортируем узлы интерполирования по расстоянию от точки x
    z1 = [(abs(z[i] - x0), z[i]) for i in range(points_count)]
    z1.sort()
    z = list(map(lambda p: p[1], z1))
    y = [f(z[i]) for i in range(points_count)]
    print('Набор узлов, ближайших к точке x, по которым будет строиться интерполяционный многочлен. Также их значения')
    for j in range(points_count):
        print(f'f({z[j]}) = {y[j]}')

    if last_point == x0 and not is_first_iteration:
        newton_interpolator.calculate_polynomial_value_at_point(n, x0)
    else:
        newton_interpolator.reform_separated_differences_table(z, y)

    approximate_lagrange_value = new_lagrange(n, z, x0)

    print(f'Значение интерполяционного многочлена в форме Лагранжа P(x) = {approximate_lagrange_value}')
    print(f'Погрешность ef(x) = {abs(f(x0) - approximate_lagrange_value)}')

    approximate_newton_value = newton_interpolator.calculate_polynomial_value_at_point(n, x0)

    print(f'Значение интерполяционного многочлена в форме Ньютона P(x) = {approximate_newton_value}')
    print(f'Погрешность ef(x) = {abs(f(x0) - approximate_newton_value)}')

    is_first_iteration = False
    last_point = x0

    print('\n')
    is_program_over = int(input('Для завершения программы введите -1. Для продолжения введите 0\n')) == -1
