from task_2_export_functions import get_interpolation_table, print_interpolation_table
from numerical_differentiation import f, form_function_derivatives_table

print('Задача численного дифференцирования')
print('Вариант 9')

is_program_over = False
while not is_program_over:
    points_count = int(input('Введите количество узлов интерполяции: m + 1 = '))
    while points_count < 3:
        print('\nДля расчета производных с погрешностью O(h^2) количество точек должно быть не меньше 3.')
        points_count = int(input('Введите количество узлов интерполяции: m + 1 = '))
    a = float(input('Введите начальную точку: a = '))
    h = float(input('Введите шаг для точек: h = '))

    func_table = get_interpolation_table(a, h, points_count, f)

    print('\nТаблица значений функции: ')
    print_interpolation_table(func_table)

    print('\nРезультаты: ')
    form_function_derivatives_table(func_table)

    print('\n')
    is_program_over = int(input('Для завершения программы введите -1. Для продолжения введите 0\n')) == -1
