from task_4_1 import *


def compound_left_rectangles_method(f, a, b, m):
    h = (b - a) / m
    y = [a + j * h for j in range(m + 1)]
    return sum([left_rectangle_method(f, y[j], y[j + 1]) for j in range(m)])
    # return h * sum([f(y[j]) for j in range(m)])


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
    pass


def compound_quadrature_38(f, a, b, m):
    pass


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

        J = accurate_integral_value(a, b)

        print(f'Интеграл f по [a, b] = {J} (точное значение)')
        print()

        left_rectangle_integral = IntegrateResult(integral := compound_left_rectangles_method(f, a, b, m),
                                                  abs(J - integral))
        right_rectangle_integral = IntegrateResult(integral := compound_right_rectangles_method(f, a, b, m),
                                                   abs(J - integral))
        middle_rectangle_integral = IntegrateResult(integral := compound_middle_rectangles_method(f, a, b, m),
                                                    abs(J - integral))
        trapezoids_integral = IntegrateResult(integral := compound_trapezoids_method(f, a, b, m), abs(J - integral))
        # parabola_integral = IntegrateResult(integral := compound_parabola_quadrature(f, a, b, m), abs(J - integral))
        # integral_38 = IntegrateResult(integral := compound_quadrature_38(f, a, b, m), abs(J - integral))

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

        # print(f'Интеграл f по [a, b] = {parabola_integral.value} (формула Симпсона (параболы))')
        # print(f'Погрешность абсолютная = {parabola_integral.error}')
        # print(f'Погрешность относительная = {parabola_integral.error / J}\n')
        #
        # print(f'Интеграл f по [a, b] = {integral_38.value} (формула 3/8)')
        # print(f'Погрешность абсолютная = {integral_38.error}')
        # print(f'Погрешность относительная = {integral_38.error / J}\n')

        print('Введите 0, если хотите завершить вычисление')
        print('Для продолжения работы введите любое число')
        signal = int(input())
        if signal == 0:
            break
