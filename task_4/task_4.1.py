from math import sin, cos

from scipy.misc import derivative


class IntegrateResult:
    def __init__(self, value, error):
        self.value = round(value, 5)  # приближённое значение интеграла
        self.error = round(error, 5)  # погрешность


def f(x):
    return sin(x) * cos(x) ** 2 + x ** 2
    # return p(x, 1) # для отладки


def p(x, n):  # многочлен степени n
    return sum([x ** i for i in range(n + 1)])


def left_rectangle_method(f, a, b):
    return IntegrateResult(
        f(a) * (b - a),
        0.5 * (b - a) ** 2 * derivative(f, (a + b) / 2)
    )


def right_rectangle_method(f, a, b):
    return IntegrateResult(
        f(b) * (b - a),
        -0.5 * (b - a) ** 2 * derivative(f, (a + b / 2))
    )


def middle_rectangle_method(f, a, b):
    return IntegrateResult(
        f((a + b) / 2) * (b - a),
        (b - a) ** 3 / 24 * derivative(f, (a + b) / 2, n=2)
    )


def trapezoids_method(f, a, b):
    return IntegrateResult(
        ((f(a) + f(b)) / 2) * (b - a),
        -(b - a) ** 3 / 12 * derivative(f, (a + b) / 2, n=2)
    )


print('Задача приближённого вычисления определённого интеграла')
print('Вариант 9')

print('Введите пределы интегрирования: ')
a = float(input('A = '))
b = float(input('B = '))

# точное значение интеграла f(x) на [a, b], вычисленное вручную
J = (1 / 3) * (b ** 3 - a ** 3) - (1 / 4) * (cos(b) - cos(a)) - (1 / 12) * (cos(3 * b) - cos(3 * a))
print(f'Интеграл f по [a, b] = {J} (точное значение)')
print()

left_rectangle_integral = left_rectangle_method(f, a, b)
right_rectangle_integral = right_rectangle_method(f, a, b)
middle_rectangle_integral = middle_rectangle_method(f, a, b)
trapezoids_integral = trapezoids_method(f, a, b)

print(f'Интеграл f по [a, b] = {left_rectangle_integral.value} (формула левого прямоугольника)')
print(f'Погрешность = {left_rectangle_integral.error}')
print(f'Интеграл f по [a, b] = {right_rectangle_integral.value} (формула правого прямоугольника)')
print(f'Погрешность = {right_rectangle_integral.error}')
print(f'Интеграл f по [a, b] = {middle_rectangle_integral.value} (формула среднего прямоугольника)')
print(f'Погрешность = {middle_rectangle_integral.error}')
print(f'Интеграл f по [a, b] = {trapezoids_integral.value} (формула трапеций)')
print(f'Погрешность = {trapezoids_integral.error}')