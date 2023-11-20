from scipy import integrate, linalg
from math import sin


def f(x_):
    return sin(x_)


def p(x_):
    return 1 / (x_ + 0.1)


def moment(n, a, b):
    return integrate.quad(lambda x_: p(x_) * (x_ ** n), a, b)[0]


print('Задача приближённого вычисления определённого интеграла с помощью ИКФ')
print('Вариант 9')

while True:
    print('Введите отрезок интегрирования:')
    A = float(input('A = '))
    B = float(input('B = '))
    print('Введите количество узлов интерполяции:')
    N = int(input('N = '))
    h = (B - A) / N
    x = [A + k * h for k in range(N)]
    C = [[x[j] ** i for j in range(N)] for i in range(N)]
    d = [round(moment(i, A, B), 3) for i in range(N)]
    a = linalg.solve(C, d)
    J_approximate = sum([a[k] * f(x[k]) for k in range(N)])
    J = integrate.quad(lambda x_: f(x_) * p(x_), A, B)[0]

    print(f'Точное значение интеграла = {J}')
    print(f'Приближённое значение интеграла = {J_approximate}')
    print(f'Погрешность = {abs(J - J_approximate)}')