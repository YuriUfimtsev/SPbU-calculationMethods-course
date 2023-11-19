from task_4_1 import *


def compound_left_rectangles_method(f, a, b, m):
    h = (b - a) / m
    y = [a + j * h for j in range(m + 1)]
    return sum([left_rectangle_method(f, y[j], y[j + 1]) for j in range(m)])
    # return h * sum([f(y[j]) for j in range(m)])


def optimized_left_rectangles_method(f0, w, h):
    return h * (w + f0)


def optimized_right_rectangles_method(fm, w, h):
    return h * (w + fm)


def optimized_middle_rectangles_method(h, q):
    return h * q


def optimized_trapezoids_method(z, w, h):
    return h / 2 * (z + 2 * w)


def optimized_parabola_quadrature(h, z, w, q):
    return (h / 6) * (z + 2 * w + 4 * q)


def compound_right_rectangles_method(f, a, b, m):
    h = (b - a) / m
    y = [a + j * h for j in range(m + 1)]
    return sum([right_rectangle_method(f, y[j], y[j + 1]) for j in range(m)])


def compound_middle_rectangles_method(f, a, b, m):
    h = (b - a) / m
    y = [a + j * h for j in range(m + 1)]
    return sum([middle_rectangle_method(f, y[j], y[j + 1]) for j in range(m)])


def compound_trapezoids_method(f, a, b, m):
    h = (b - a) / m
    y = [a + j * h for j in range(m + 1)]
    return sum([trapezoids_method(f, y[j], y[j + 1]) for j in range(m)])


def compound_parabola_quadrature(f, a, b, m):
    h = (b - a) / m
    y = [a + j * h for j in range(m + 1)]
    return sum([parabola_quadrature(f, y[j], y[j + 1]) for j in range(m)])


if __name__ == "__main__":
    print('Задача приближённого вычисления определённого интеграла по составным квадратурным формулам')
    print('Вариант 9')
    print(f'f(x) = sin(x) * cos(x)^2 + x^2')

    while True:
        print('Введите пределы интегрирования: ')
        a = float(input('A = '))
        b = float(input('B = '))
        print('Введите количество точек разбиения: ')
        m = int(input('m = '))

        # точное значение интеграла f(x) на [a, b], вычисленное вручную
        J = accurate_integral_value(a, b)
        # J = b - a # если f = const = 1
        # J = (1 / 2) * (b ** 2 - a ** 2) # если f = x
        # J = (1 / 3) * (b ** 3 - a ** 3) # если f = x^2
        # J = (1 / 4) * (b ** 4 - a ** 4) # если f = x^3


        print(f'Интеграл f по [a, b] = {J} (точное значение, p = 1)')
        print()

        h = (b - a) / m
        x = [a + j * h for j in range(m + 1)]
        w = sum([f(x[j]) for j in range(1, m)])
        f0 = f(x[0])
        fm = f(x[m])
        z = f(x[0]) + f(x[m])
        q = sum([f(x[j] + h / 2) for j in range(m)])

        # left_rectangle_integral = IntegrateResult(integral := compound_left_rectangles_method(f, a, b, m),
        #                                           abs(J - integral))
        # right_rectangle_integral = IntegrateResult(integral := compound_right_rectangles_method(f, a, b, m),
        #                                            abs(J - integral))
        # middle_rectangle_integral = IntegrateResult(integral := compound_middle_rectangles_method(f, a, b, m),
        #                                             abs(J - integral))
        # trapezoids_integral = IntegrateResult(integral := compound_trapezoids_method(f, a, b, m), abs(J - integral))
        # parabola_integral = IntegrateResult(integral := compound_parabola_quadrature(f, a, b, m), abs(J - integral))

        left_rectangle_integral = IntegrateResult(integral := optimized_left_rectangles_method(f0, w, h),
                                                  abs(J - integral))
        right_rectangle_integral = IntegrateResult(integral := optimized_right_rectangles_method(fm, w, h),
                                                   abs(J - integral))
        middle_rectangle_integral = IntegrateResult(integral := optimized_middle_rectangles_method(h, q),
                                                    abs(J - integral))
        trapezoids_integral = IntegrateResult(integral := optimized_trapezoids_method(z, w, h), abs(J - integral))
        parabola_integral = IntegrateResult(integral := optimized_parabola_quadrature(h, z, w, q), abs(J - integral))

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

        print('Введите 0, если хотите завершить вычисление')
        print('Для продолжения работы введите любое число')
        signal = int(input())
        if signal == 0:
            break
