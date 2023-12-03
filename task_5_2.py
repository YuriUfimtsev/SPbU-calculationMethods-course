from math import sin, pi, cos
from scipy import integrate


def f(x):
    return sin(x ** 2)


def P(n, x):
    if n == 0:
        return 1
    if n == 1:
        return x
    return (2 * n - 1) / n * P(n - 1, x) * x - (n - 1) / n * P(n - 2, x)


def P_derivative(n, x):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (2 * n - 1) / n * (P_derivative(n - 1, x) * x + P(n - 1, x)) - (n - 1) / n * P_derivative(n - 2, x)


def find_P_roots(n, eps=10 ** -12):
    roots = []
    for i in range(1, n + 1):
        x0 = cos(pi * (4 * i - 1) / (4 * n + 2))
        while abs(P(n, x0)) > eps:
            x0 = x0 - P(n, x0) / P_derivative(n, x0)
        roots.append(x0)
    return roots


def Gaussian_integral(f, a, b, x, A):
    n = len(A)
    t = [(b - a) / 2 * x[k] + (b + a) / 2 for k in range(n)]
    return (b - a) / 2 * sum([A[k] * f(t[k]) for k in range(n)])


print('Задача нахождения определённого интеграла при помощи КФ Гаусса')
print('Вариант 9')
print('f(x) = sin(x^2)')
print('a = 0; b = π/4')

a = 0
b = pi / 4

xs = {}  # xs[n] = список узлов x_1, ..., x_n для квадратурной формы порядка n
coefficients = {}  # coefficients[n] = список коэффициентов A_1, ..., A_n для квадратурной формулы порядка n

for N in range(1, 9):
    print(f'\nN = {N}:')
    x = find_P_roots(N, 10 ** -12)
    A = [2 * (1 - x[k] ** 2) / (N ** 2 * (P(N - 1, x[k])) ** 2) for k in range(len(x))]
    for k in range(len(x)):
        print(f'    x{k + 1} = {x[k]} --> A{k + 1} = {A[k]}')
    xs[N] = x
    coefficients[N] = A

print()
# проверка точности формулы на многочленах
for N in [6, 7, 8]:
    check_degree = 2 * N - 1
    p = lambda y: y ** check_degree
    integral = b ** (check_degree + 1) / (check_degree + 1) - a ** (check_degree + 1) / (check_degree + 1)
    approx_integral = Gaussian_integral(p, a, b, xs[N], coefficients[N])
    print(f'Погрешность КФ Гаусса для N = {N} (интеграл x^{check_degree} от a до b)'
          f' = {abs(integral - approx_integral)}')

while True:
    print('\nВведите значения N1, N2, N3: ')
    N1 = int(input('N1 = '))
    N2 = int(input('N2 = '))
    N3 = int(input('N3 = '))

    integral = integrate.quad(f, a, b)[0]  # точное значение интеграла
    for t in [N1, N2, N3]:
        if t > len(xs):
            x = find_P_roots(t, 10 ** -12)
            A = [2 * (1 - x[k] ** 2) / (t ** 2 * (P(t - 1, x[k])) ** 2) for k in range(len(x))]
            xs[t] = x
            coefficients[t] = A
        print(f'\n Узлы и коэффициенты КФ Гаусса с {t} узлами')
        for k in range(len(x)):
            print(f'    x{k + 1} = {x[k]} --> A{k + 1} = {A[k]}')

    approx_integral_1 = Gaussian_integral(f, a, b, xs[N1], coefficients[N1])
    approx_integral_2 = Gaussian_integral(f, a, b, xs[N2], coefficients[N2])
    approx_integral_3 = Gaussian_integral(f, a, b, xs[N3], coefficients[N3])

    print(f'Точное значение интеграла f(x) от {a} до {b} = {integral}')
    print(f'\nПриближённое значение интеграла f(x) от {a} до {b} по КФ Гаусса порядка {N1} = {approx_integral_1}')
    print(f'Погрешность абсолютная = {abs(integral - approx_integral_1)}')
    print(f'\nПриближённое значение интеграла f(x) от {a} до {b} по КФ Гаусса порядка {N2} = {approx_integral_2}')
    print(f'Погрешность абсолютная = {abs(integral - approx_integral_2)}')
    print(f'\nПриближённое значение интеграла f(x) от {a} до {b} по КФ Гаусса порядка {N3} = {approx_integral_3}')
    print(f'Погрешность абсолютная = {abs(integral - approx_integral_3)}')

    print('\nЕсли вы хотите закончить вычисления, введите 0')
    print('Для продолжения введите любое число')
    signal = int(input())

    if signal == 0:
        break

    print('Введите пределы интегрирования: ')
    a = float(input('A = '))
    b = float(input('B = '))
