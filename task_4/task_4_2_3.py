from task_4_1 import *


def compound_left_rectangles_method(f, a, b, m):
    h = (b - a) / m
    y = [a + j * h for j in range(m + 1)]
    return sum([left_rectangle_method(f, y[j], y[j + 1]) for j in range(m)])


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


def calculate_and_print_integral_value(_a, _b, _m, _f):
    h = (_b - _a) / _m
    x = [_a + j * h for j in range(_m + 1)]
    w = sum([f(x[j]) for j in range(1, _m)])
    f0 = _f(x[0])
    fm = _f(x[_m])
    z = f(x[0]) + f(x[m])
    q = sum([f(x[j] + h / 2) for j in range(_m)])

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

    return [left_rectangle_integral.value, right_rectangle_integral.value,
            middle_rectangle_integral.value, trapezoids_integral.value, parabola_integral.value]


def clarify_value(value, more_accurate_value, _l, d):
    r = d + 1
    return ((_l ** r) * more_accurate_value - value) / ((_l ** r) - 1)


def clarify_values_and_print_errors(values_array, more_accurate_values_array, _l):
    left_rectangle_integral_clarified = IntegrateResult(integral := clarify_value(values_array[0],
                                                                                  more_accurate_values_array[0], _l,
                                                                                  0),
                                                        abs(J - integral))
    right_rectangle_integral_clarified = IntegrateResult(integral := clarify_value(values_array[1],
                                                                                   more_accurate_values_array[1], _l,
                                                                                   0),
                                                         abs(J - integral))
    middle_rectangle_integral_clarified = IntegrateResult(integral := clarify_value(values_array[2],
                                                                                    more_accurate_values_array[2], _l,
                                                                                    1),
                                                          abs(J - integral))
    trapezoids_integral_clarified = IntegrateResult(integral := clarify_value(values_array[3],
                                                                              more_accurate_values_array[3], _l, 1),
                                                    abs(J - integral))
    parabola_integral_clarified = IntegrateResult(integral := clarify_value(values_array[4],
                                                                            more_accurate_values_array[4], _l, 3),
                                                  abs(J - integral))

    print('\nУточненные значения\n')
    print(
        f'Уточненное значение интеграла f по [a, b] = {left_rectangle_integral_clarified.value}'
        f' (формула левого прямоугольника)')
    print(f'Погрешность абсолютная = {left_rectangle_integral_clarified.error}')
    print(f'Погрешность относительная = {left_rectangle_integral_clarified.error / J}\n')

    print(
        f'Уточненное значение интеграла f по [a, b] = {right_rectangle_integral_clarified.value}'
        f' (формула правого прямоугольника)')
    print(f'Погрешность абсолютная = {right_rectangle_integral_clarified.error}')
    print(f'Погрешность относительная = {right_rectangle_integral_clarified.error / J}\n')

    print(
        f'Уточненное значение интеграла f по [a, b] = {middle_rectangle_integral_clarified.value}'
        f' (формула среднего прямоугольника)')
    print(f'Погрешность абсолютная = {middle_rectangle_integral_clarified.error}')
    print(f'Погрешность относительная = {middle_rectangle_integral_clarified.error / J}\n')

    print(f'Уточненное значение интеграла f по [a, b] = {trapezoids_integral_clarified.value} (формула трапеций)')
    print(f'Погрешность абсолютная = {trapezoids_integral_clarified.error}')
    print(f'Погрешность относительная = {trapezoids_integral_clarified.error / J}\n')

    print(f'Уточненное значение интеграла f по [a, b] = {parabola_integral_clarified.value}'
          f' (формула Симпсона (параболы))')
    print(f'Погрешность абсолютная = {parabola_integral_clarified.error}')
    print(f'Погрешность относительная = {parabola_integral_clarified.error / J}\n')


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
        m_partition_results = calculate_and_print_integral_value(a, b, m, f)

        l = 0
        while l <= 0:
            print('Введите натуральное число l')
            l = int(input('l = '))

        print(f'Значения интеграла с новым числом разбиений {m * l}')
        print()
        ml_partition_results = calculate_and_print_integral_value(a, b, m * l, f)

        clarify_values_and_print_errors(m_partition_results, ml_partition_results, l)

        print('Введите 0, если хотите завершить вычисление')
        print('Для продолжения работы введите любое число')
        signal = int(input())
        if signal == 0:
            break
