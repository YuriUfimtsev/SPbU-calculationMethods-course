from task_2_newton_interpolator import NewtonInterpolator
import task_2_export_functions as func

print('Задача алгебраического интерполирования')
print('Вариант 9')

points_count = int(input('Введите количество узлов интерполяции: m + 1 = '))
print('Введите отрезок, на котором нужно интерполировать функцию: ')
A = float(input('A = '))
B = float(input('B = '))

func_table = func.get_interpolation_table(A, B - A, points_count, func.f)

print('Таблица значений функции: ')
func.print_interpolation_table(func_table)

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
    func.sort_interpolation_table(func_table, x0)

    print('Набор узлов, ближайших к точке x, по которым будет строиться интерполяционный многочлен. Также их значения')
    func.print_interpolation_table(func_table)

    if last_point == x0 and not is_first_iteration:
        newton_interpolator.calculate_polynomial_value_at_point(n, x0)
    else:
        newton_interpolator.reform_separated_differences_table(func_table)

    approximate_lagrange_value = func.Lagrange(n, list(map(lambda p: p[0], func_table)), x0)

    print(f'Значение интерполяционного многочлена в форме Лагранжа P(x) = {approximate_lagrange_value}')
    print(f'Погрешность ef(x) = {abs(func.f(x0) - approximate_lagrange_value)}')

    approximate_newton_value = newton_interpolator.calculate_polynomial_value_at_point(n, x0)

    print(f'Значение интерполяционного многочлена в форме Ньютона P(x) = {approximate_newton_value}')
    print(f'Погрешность ef(x) = {abs(func.f(x0) - approximate_newton_value)}')

    is_first_iteration = False
    last_point = x0

    print('\n')
    is_program_over = int(input('Для завершения программы введите -1. Для продолжения введите 0\n')) == -1
