from math import sin, cos


class IntegrateResult:
    def __init__(self, value, error):
        self.value = value  # приближённое значение интеграла
        self.error = error  # погрешность


def f(x):
    return sin(x) * cos(x) ** 2 + x ** 2
    # return p(x, 1) # для отладки


def p(x, n):  # многочлен степени n
    return sum([x ** i for i in range(n + 1)])


def left_rectangle_method(f, a, b):
    return f(a) * (b - a)


def right_rectangle_method(f, a, b):
    return f(b) * (b - a)


def middle_rectangle_method(f, a, b):
    return f((a + b) / 2) * (b - a)


def trapezoids_method(f, a, b):
    return ((f(a) + f(b)) / 2) * (b - a)


def parabola_quadrature(f, a, b):
    return ((b - a) / 6) * (f(a) + 4*f((a + b) / 2)) + f(b)


def quadrature_38(f, a, b):
    return (b - a) * ((1 / 8) * f(a) + (3 / 8) * f(a + (b - a) / 3) + (3 / 8) * f(a + 2 * (b - a) / 3) + (1 / 8) * f(b))


print('Задача приближённого вычисления определённого интеграла по квадратурным формулам')
print('Вариант 9')
print(f'f = sin(x) * cos(x)^2 + x^2')

print('Введите пределы интегрирования: ')
a = float(input('A = '))
b = float(input('B = '))

# точное значение интеграла f(x) на [a, b], вычисленное вручную
J = (1 / 3) * (b ** 3 - a ** 3) - (1 / 4) * (cos(b) - cos(a)) - (1 / 12) * (cos(3 * b) - cos(3 * a))
print(f'Интеграл f по [a, b] = {J} (точное значение)')
print()

left_rectangle_integral = IntegrateResult(left_rectangle_method(f, a, b), abs(J - left_rectangle_method(f, a, b)))
right_rectangle_integral = IntegrateResult(right_rectangle_method(f, a, b), abs(J - right_rectangle_method(f, a, b)))
middle_rectangle_integral = IntegrateResult(middle_rectangle_method(f, a, b), abs(J - middle_rectangle_method(f, a, b)))
trapezoids_integral = IntegrateResult(trapezoids_method(f, a, b), abs(J - trapezoids_method(f, a, b)))
parabola_integral = IntegrateResult(parabola_quadrature(f, a, b), abs(J - parabola_quadrature(f, a, b)))
integral_38 = IntegrateResult(quadrature_38(f, a, b), abs(J - quadrature_38(f, a, b)))

print(f'Интеграл f по [a, b] = {left_rectangle_integral.value} (формула левого прямоугольника)')
print(f'Погрешность = {left_rectangle_integral.error}\n')
print(f'Интеграл f по [a, b] = {right_rectangle_integral.value} (формула правого прямоугольника)')
print(f'Погрешность = {right_rectangle_integral.error}\n')
print(f'Интеграл f по [a, b] = {middle_rectangle_integral.value} (формула среднего прямоугольника)')
print(f'Погрешность = {middle_rectangle_integral.error}\n')
print(f'Интеграл f по [a, b] = {trapezoids_integral.value} (формула трапеций)')
print(f'Погрешность = {trapezoids_integral.error}\n')
print(f'Интеграл f по [a, b] = {parabola_integral.value} (формула Симпсона (параболы))')
print(f'Погрешность = {parabola_integral.error}\n')
print(f'Интеграл f по [a, b] = {integral_38.value} (формула 3/8)')
print(f'Погрешность = {integral_38.error}\n')
