from math import sin, cos


class IntegrateResult:
    def __init__(self, value, error):
        self.value = value  # приближённое значение интеграла
        self.error = error  # погрешность


def f(x):
    return sin(x) * cos(x) ** 2 + x ** 2
    # return p(x, 0)
    # return p(x, 1) # для отладки
    # return p(x, 2)
    # return p(x, 3)
    # return p(x, 4)


# точное значение интеграла f(x) на [a, b], вычисленное вручную
def accurate_integral_value(a, b):
    return (1 / 3) * (b ** 3 - a ** 3) - (1 / 4) * (cos(b) - cos(a)) - (1 / 12) * (cos(3 * b) - cos(3 * a))


def p(x, n):  # многочлен степени n
    return x ** n


def left_rectangle_method(f, a, b):
    return f(a) * (b - a)


def right_rectangle_method(f, a, b):
    return f(b) * (b - a)


def middle_rectangle_method(f, a, b):
    return f((a + b) / 2) * (b - a)


def trapezoids_method(f, a, b):
    return ((f(a) + f(b)) / 2) * (b - a)


def parabola_quadrature(f, a, b):
    return ((b - a) / 6) * (f(a) + 4 * f((a + b) / 2) + f(b))


def quadrature_38(f, a, b):
    return (b - a) * ((1 / 8) * f(a) + (3 / 8) * f(a + (b - a) / 3) + (3 / 8) * f(a + 2 * (b - a) / 3) + (1 / 8) * f(b))


if __name__ == "__main__":

    print('Задача приближённого вычисления определённого интеграла по квадратурным формулам')
    print('Вариант 9')
    print(f'f(x) = sin(x) * cos(x)^2 + x^2')

    while True:
        print('Введите пределы интегрирования: ')
        a = float(input('A = '))
        b = float(input('B = '))

        # точное значение интеграла f(x) на [a, b], вычисленное вручную
        J = accurate_integral_value(a, b)
        # J = b - a # если f = const = 1
        # J = (1 / 2) * (b ** 2 - a ** 2) # если f = x
        # J = (1 / 3) * (b ** 3 - a ** 3) # если f = x^2
        # J = (1 / 4) * (b ** 4 - a ** 4) # если f = x^3
        # J = (1 / 5) * (b ** 5 - a ** 5) # если f = x^4

        print(f'Интеграл f по [a, b] = {J} (точное значение)')
        print()

        left_rectangle_integral = IntegrateResult(left_rectangle_method(f, a, b),
                                                  abs(J - left_rectangle_method(f, a, b)))
        right_rectangle_integral = IntegrateResult(right_rectangle_method(f, a, b),
                                                   abs(J - right_rectangle_method(f, a, b)))
        middle_rectangle_integral = IntegrateResult(middle_rectangle_method(f, a, b),
                                                    abs(J - middle_rectangle_method(f, a, b)))
        trapezoids_integral = IntegrateResult(trapezoids_method(f, a, b), abs(J - trapezoids_method(f, a, b)))
        parabola_integral = IntegrateResult(parabola_quadrature(f, a, b), abs(J - parabola_quadrature(f, a, b)))
        integral_38 = IntegrateResult(quadrature_38(f, a, b), abs(J - quadrature_38(f, a, b)))

        print(f'Интеграл f по [a, b] = {left_rectangle_integral.value} (формула левого прямоугольника)')
        print(f'Погрешность абсолютная = {left_rectangle_integral.error}')
        print(f'Погрешность относительная = {left_rectangle_integral.error / J}\n')

        print(f'Интеграл f по [a, b] = {right_rectangle_integral.value} (формула правого прямоугольника)')
        print(f'Погрешность абсолютная = {right_rectangle_integral.error}')
        print(f'Погрешность относительная = {right_rectangle_integral.error / J}\n')

        print(f'Интеграл f по [a, b] = {middle_rectangle_integral.value} (формула среднего прямоугольника)')
        print(f'Погрешность абсолютная = {middle_rectangle_integral.error}')
        print(f'Погрешность относительная = {middle_rectangle_integral.error / J}\n')

        print(f'Интеграл f по [a, b] = {trapezoids_integral.value} (формула трапеций)')
        print(f'Погрешность абсолютная = {trapezoids_integral.error}')
        print(f'Погрешность относительная = {trapezoids_integral.error / J}\n')

        print(f'Интеграл f по [a, b] = {parabola_integral.value} (формула Симпсона (параболы))')
        print(f'Погрешность абсолютная = {parabola_integral.error}')
        print(f'Погрешность относительная = {parabola_integral.error / J}\n')

        print(f'Интеграл f по [a, b] = {integral_38.value} (формула 3/8)')
        print(f'Погрешность абсолютная = {integral_38.error}')
        print(f'Погрешность относительная = {integral_38.error / J}\n')

        print('Введите 0, если хотите завершить вычисление')
        print('Для продолжения работы введите любое число')
        signal = int(input())
        if signal == 0:
            break
