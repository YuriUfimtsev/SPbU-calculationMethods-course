import polynomial as pol
from math import exp


def f(x_):
    return 1 - exp(-x_) + x_ ** 2


def product(l_):
    result = pol.Polynomial(1)
    for i in range(len(l_)):
        result *= l_[i]
    return result


def w(n_, z_):
    return product([pol.Polynomial(1, -z_[k]) for k in range(n_ + 1)])


def l(k, n_, z_):
    return w(n_, z_) // (pol.Polynomial(1, -z_[k]) * w(n_, z_).derivative.calculate(z_[k]))


def L(n_, z_):
    result = pol.Polynomial(0)
    for k in range(n_ + 1):
        result += pol.Polynomial(f(z_[k])) * l(k, n_, z_)
    return result


def Lagrange(n_, z_, x_):
    return L(n_, z_).calculate(x_)


class NewtonInterpolator:
    def __init__(self, points, function_in_points):
        self.points = points
        self.table = [[0.0] * (len(points) + 1) for _ in range(len(points) * 2 - 1)]
        for i in range(0, len(self.table), 2):
            self.table[i][0] = points[i // 2]
            self.table[i][1] = function_in_points[i // 2]
            self.polynomial = pol.Polynomial()

        row_offset = 0
        for k in range(2, len(self.table[0]), 1):
            row_offset += 1
            for i in range(row_offset, len(self.table) - row_offset, 2):
                self.table[i][k] = ((self.table[i + 1][k - 1] - self.table[i - 1][k - 1])
                                    / (self.table[i + (k - 1)][0] - self.table[i - (k - 1)][0]))

    def _form_polynomial(self, polynomial_degree):
        def get_pol_multiplier(degree_number):
            multiplier = pol.Polynomial(1)
            for p in range(0, degree_number):
                multiplier *= pol.Polynomial(1, -1 * self.table[p * 2][0])
            return multiplier

        result = self.table[0][1] * pol.Polynomial(1)
        for i in range(1, polynomial_degree + 1):
            result += self.table[i][i + 1] * get_pol_multiplier(i)
        self.polynomial = result

    def calculate_polynomial_value_at_point(self, polynomial_degree, x):
        if self.polynomial.degree != polynomial_degree:
            self._form_polynomial(polynomial_degree)
        return self.polynomial.calculate(x)


def product(l_):
    result = pol.Polynomial(1)
    for i in range(len(l_)):
        result *= l_[i]
    return result


def w(n_, z_):
    return product([pol.Polynomial(1, -z_[k]) for k in range(n_ + 1)])


def l(k, n_, z_):
    return w(n_, z_) // (pol.Polynomial(1, -z_[k]) * w(n_, z_).derivative.calculate(z_[k]))


def L(n_, z_):
    result = pol.Polynomial(0)
    for k in range(n_ + 1):
        result += pol.Polynomial(f(z_[k])) * l(k, n_, z_)
    return result


print('Задача алгебраического интерполирования')
print('Вариант 9')

points_count = int(input('Введите количество узлов интерполяции: m + 1 = '))
print('Введите отрезок, на котором нужно интерполировать функцию: ')
A = float(input('A = '))
B = float(input('B = '))

z = [A + i * (B - A) / points_count for i in range(points_count)]  # узлы интерполяции
y = [f(z[i]) for i in range(points_count)]
print('Таблица значений функции: ')
for j in range(points_count):
    print(f'f(z{j}) = {y[j]}')

newton_interpolator = NewtonInterpolator(z, y)
is_over = 0
while is_over == 0:
    x0 = float(input('Введите точку интерполирования: x = '))
    n = int(input(f'Введите степень интерполяционного многочлена не выше {points_count - 1}: n = '))
    while n >= points_count:
        n = int(input(f'Введено недопустимое значение. Введите степень интерполяционного многочлена не выше'
                      f'{points_count - 1}: n = '))

    # сортируем узлы интерполирования по расстоянию от точки x
    z1 = [(abs(z[i] - x0), z[i]) for i in range(points_count)]
    z1.sort()
    z = list(map(lambda p: p[1], z1))
    y = [f(z[i]) for i in range(points_count)]
    print('Набор узлов, ближайших к точке x, по которым будет строиться интерполяционный многочлен. Также их значения')
    for j in range(points_count):
        print(f'f({z[j]}) = {y[j]}')

    approximate_lagrange_value = L(n, z).calculate(x0)

    print(f'Значение интерполяционного многочлена в форме Лагранжа P(x) = {approximate_lagrange_value}')
    print(f'Погрешность ef(x) = {abs(f(x0) - approximate_lagrange_value)}')

    approximate_newton_value = newton_interpolator.calculate_polynomial_value_at_point(n, x0)

    print(f'Значение интерполяционного многочлена в форме Ньютона P(x) = {approximate_newton_value}')
    print(f'Погрешность ef(x) = {abs(f(x0) - approximate_newton_value)}')
    print('\n')
    is_over = int(input('Для завершения программы введите -1. Для продолжения введите 0\n'))
