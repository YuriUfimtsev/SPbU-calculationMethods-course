import numpy
from scipy import integrate, linalg
from numpy import polynomial as pol
from iqf import p, f, moment


def get_orthogonal_polynom(moments):
    nodes_count = int(len(moments) / 2)
    moment_matrix = [[moments[j] for j in range(i, i + nodes_count)] for i in range(nodes_count)]
    _moment_column = [-1 * moments[i] for i in range(nodes_count, nodes_count * 2)]
    orthogonal_polynom_coefficients = linalg.solve(moment_matrix, _moment_column)
    _orthogonal_polynom = pol.polynomial.Polynomial(numpy.append(orthogonal_polynom_coefficients, 1))
    return _orthogonal_polynom


def test_on_polynom(nodes, coefficients, weight, _a, _b):
    polynom_degree = 2 * len(nodes) - 1
    integral_result = integrate.quad(lambda x_: (x_**polynom_degree) * weight(x_), _a, _b)[0]
    iqf_result = sum([coefficients[k] * (nodes[k]**polynom_degree) for k in range(len(nodes))])
    error = abs(integral_result - iqf_result)
    return error < 0.1**10


while True:
    print('\nВведите отрезок интегрирования:')
    A = float(input('A = '))
    B = float(input('B = '))
    print('Введите количество узлов интерполирования:')
    N = int(input('N = '))
    if N < 2:
        raise ValueError("Количество узлов интерполяции должно быть не меньше двух!")

    d = [moment(i, A, B) for i in range(2 * N)]
    print('\nМоменты весовой функции:')
    for i in range(2 * N):
        print(f'μ{i} = {d[i]}')

    orthogonal_polynom = get_orthogonal_polynom(d)
    print(f'\nОртогональный многочлен: {str(orthogonal_polynom)}')

    roots = orthogonal_polynom.roots()
    print('\nУзлы КФ:')
    for i in range(len(roots)):
        print(roots[i])

    C = [[round(roots[j] ** i, 20) for j in range(N)] for i in range(N)]
    moment_column = [d[i] for i in range(N)]
    a = linalg.solve(C, moment_column)
    print('\nКоэффициенты КФ:')
    for i in range(len(a)):
        print(f'a{i} = {a[i]}')
        if a[i] <= 0:
            raise ValueError("Тест на положительне коэффициенты не пройден")

    if not test_on_polynom(roots, a, p, A, B):
        raise ValueError("Тест на многочлене не пройден")

    J_approximate = sum([a[k] * f(roots[k]) for k in range(N)])

    J = integrate.quad(lambda x_: f(x_) * p(x_), A, B)[0]

    print(f'\nТочное значение интеграла = {J}')
    print(f'Приближённое значение интеграла = {J_approximate}')
    print(f'Погрешность абсолютная = {abs(J - J_approximate)}')
    print(f'Погрешность относительная = {abs(J - J_approximate)/abs(J)}')

    print('\nЧтобы закончить вычисления, введите 0')
    print('Чтобы продолжить, введите любое число')

    flag = int(input())
    if flag == 0:
        break
