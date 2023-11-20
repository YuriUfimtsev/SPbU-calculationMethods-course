from scipy import integrate, linalg
from math import sin
import polynomial as pol


def f(x_):
    return sin(x_)


def p(x_):
    return 1 / (x_ + 0.1)


def moment(n, a, b):
    return integrate.quad(lambda x_: p(x_) * (x_ ** n), a, b)[0]


def polynom_accuracy_check(N, A, B, x):
    def polynom_N(x):
        # 1 + x + x^2 + ... + x^(N - 1)
        return sum([x ** i for i in range(N)])

    C = [[x[j] ** i for j in range(N)] for i in range(N)]
    d = [round(moment(i, A, B), 3) for i in range(N)]
    integral = sum([1 / (r + 1) * (B ** (r + 1) - A ** (r + 1)) for r in range(N)])
    a = linalg.solve(C, d)
    approximate_integral = sum([a[k] * x[k] for k in range(N)])
    print(f'Погрешность = {abs(integral - approximate_integral)}')



print('Задача приближённого вычисления определённого интеграла с помощью ИКФ')
print('Вариант 9')
print('f(x) = sin(x)')
print('ρ(x) = 1 / (x + 0.1)')

while True:
    print('Введите отрезок интегрирования:')
    A = float(input('A = '))
    B = float(input('B = '))
    print('Введите количество узлов интерполяции:')
    N = int(input('N = '))
    if N < 2:
        raise ValueError("Количество узлов интерполяции должно быть больше двух!")
    print('Введите узлы интерполяции через пробел:')
    x = [float(i) for i in input().split()]
    if len(x) != len(set(x)):
        raise ValueError("Узлы интерполяции должны быть различными!")
    C = [[x[j] ** i for j in range(N)] for i in range(N)]
    d = [round(moment(i, A, B), 3) for i in range(N)]
    print('Моменты весовой функции:')
    for i in range(N):
        print(f'μ{i} = {d[i]}')
    a = linalg.solve(C, d)
    print('Коэффициенты КФ:')
    for i in range(len(a)):
        print(f'a{i} = {round(a[i], 3)}')
    J_approximate = sum([a[k] * f(x[k]) for k in range(N)])
    J = integrate.quad(lambda x_: f(x_) * p(x_), A, B)[0]

    print(f'Точное значение интеграла = {J}')
    print(f'Приближённое значение интеграла = {J_approximate}')
    print(f'Погрешность = {abs(J - J_approximate)}')

    print('Чтобы закончить вычисления, введите 0')
    print('Чтобы продолжить, введите любое число')

    flag = int(input())
    if flag == 0:
        break
