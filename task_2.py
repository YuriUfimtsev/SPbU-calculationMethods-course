import polynomial as pol
from task_2_newton_interpolator import NewtonInterpolator
from math import exp


def f(x_):
    return 1 - exp(-x_) + x_ ** 2


def Lagrange(n_, z_, x):
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


def get_interpolation_table(a, h, points_count_, func):
    """
    Generates a table with interpolation nodes and function values in these nodes.
    Based on start of the segment and step.
    """
    return [(a + i * h / (points_count_ - 1),
             func(a + i * h / (points_count_ - 1))) for i in range(points_count_)]


def sort_interpolation_table(interpolation_table, x):
    """
    Sorts a table with interpolation nodes and function values in these nodes.
    Nodes are ordered by proximity to a point x.
    """
    return interpolation_table.sort(key=lambda array: abs(array[0] - x))


def print_interpolation_table(interpolation_table):
    """
    Prints a table with interpolation nodes and function values in these nodes.
    """
    for j in range(len(interpolation_table)):
        print(f'f({interpolation_table[j][0]}) = {interpolation_table[j][1]}')


print('Задача алгебраического интерполирования')
print('Вариант 9')

points_count = int(input('Введите количество узлов интерполяции: m + 1 = '))
print('Введите отрезок, на котором нужно интерполировать функцию: ')
A = float(input('A = '))
B = float(input('B = '))

func_table = get_interpolation_table(A, B - A, points_count, f)

print('Таблица значений функции: ')
print_interpolation_table(func_table)

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
    sort_interpolation_table(func_table, x0)

    print('Набор узлов, ближайших к точке x, по которым будет строиться интерполяционный многочлен. Также их значения')
    print_interpolation_table(func_table)

    if last_point == x0 and not is_first_iteration:
        newton_interpolator.calculate_polynomial_value_at_point(n, x0)
    else:
        newton_interpolator.reform_separated_differences_table(func_table)

    approximate_lagrange_value = Lagrange(n, list(map(lambda p: p[0], func_table)), x0)

    print(f'Значение интерполяционного многочлена в форме Лагранжа P(x) = {approximate_lagrange_value}')
    print(f'Погрешность ef(x) = {abs(f(x0) - approximate_lagrange_value)}')

    approximate_newton_value = newton_interpolator.calculate_polynomial_value_at_point(n, x0)

    print(f'Значение интерполяционного многочлена в форме Ньютона P(x) = {approximate_newton_value}')
    print(f'Погрешность ef(x) = {abs(f(x0) - approximate_newton_value)}')

    is_first_iteration = False
    last_point = x0

    print('\n')
    is_program_over = int(input('Для завершения программы введите -1. Для продолжения введите 0\n')) == -1
