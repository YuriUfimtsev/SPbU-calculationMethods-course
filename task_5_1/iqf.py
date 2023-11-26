from scipy import integrate, linalg
from math import sin


def f(x_):
    return sin(x_)


def p(x_):
    return 1 / (x_ + 0.1)


def moment(n, _a, _b):
    return integrate.quad(lambda x_: p(x_) * (x_ ** n), _a, _b)[0]


def calculate_interpolation_nodes(_a, _b, n):
    _h = (_b - _a) / (n + 2)
    return [_a + j * _h for j in range(1, n + 1)]


def test_on_polynom(nodes, coefficients, weight, _a, _b):
    polynom_degree = len(nodes) - 1
    integral_result = integrate.quad(lambda x_: (x_**polynom_degree) * weight(x_), _a, _b)[0]
    iqf_result = sum([coefficients[k] * (nodes[k]**polynom_degree) for k in range(len(nodes))])
    error = abs(integral_result - iqf_result)
    return error < 0.1**10


print('Задача приближённого вычисления определённого интеграла с помощью ИКФ и ИКФ НАСТ')
print('Вариант 9')
print('f(x) = sin(x)')
print('ρ(x) = 1 / (x + 0.1)')


if __name__ == "__main__":
    while True:
        print('Введите отрезок интегрирования:')
        A = float(input('A = '))
        B = float(input('B = '))
        print('Введите количество узлов интерполяции:')
        N = int(input('N = '))
        if N < 2:
            raise ValueError("Количество узлов интерполяции должно быть не меньше двух!")

        print('\nУзлы интерполяции:')
        x = calculate_interpolation_nodes(A, B, N)
        for i in range(len(x)):
            print(x[i])

        C = [[round(x[j] ** i, 20) for j in range(N)] for i in range(N)]
        d = [moment(i, A, B) for i in range(N)]
        print('\nМоменты весовой функции:')
        for i in range(N):
            print(f'μ{i} = {d[i]}')

        a = linalg.solve(C, d)

        print('\nКоэффициенты КФ:')
        for i in range(len(a)):
            print(f'a{i} = {a[i]}')

        if not test_on_polynom(x, a, p, A, B):
            raise ValueError("Тест на многочлене не пройден")

        J_approximate = sum([a[k] * f(x[k]) for k in range(N)])

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
