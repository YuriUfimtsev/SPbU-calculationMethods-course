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


# deg -- степень многочлена Лежандра
# def get_roots_segments(A, B, N_roots, deg):
#     h = (B - A) / N_roots
#     control_points = [A + i * h for i in range(0, N_roots + 1)]
#     segments = []
#     for i in range(1, N_roots + 1):
#         c, d = control_points[i - 1], control_points[i]
#         if P(deg, c) * P(deg, d) < 0:
#             segments.append((c, d))
#     return segments
#
#
# def secant(segment, deg, eps=10 ** -12):
#     a, b = segment[0], segment[1]
#     x = [a, b]
#     while abs(x[-1] - x[-2]) >= eps:
#         x.append(x[-1] - ((x[-1] - x[-2]) * (P(deg, x[-1]) / (P(deg, x[-1]) - P(deg, x[-2])))))
#     return x[-1]


print('Задача нахождения определённого интеграла при помощи квадратурных формул Гаусса')
print('Вариант 9')
print('f(x) = sin(x^2)')
print('a = 0; b = π/4')

a = 0
b = pi / 4

xs = {}  # xs[n] = список узлов x_1, ..., x_n для квадратурной формы порядка n
coefficients = {}  # coefficients[n] = список коэффициентов A_1, ..., A_n для квадратурной формулы порядка n

for N in range(1, 9):
    print(f'N = {N}:')
    x = find_P_roots(N, 10 ** -12)
    A = [2 * (1 - x[k] ** 2) / (N ** 2 * (P(N - 1, x[k])) ** 2) for k in range(len(x))]
    for k in range(len(x)):
        print(f'    x{k + 1} = {x[k]} --> A{k + 1} = {A[k]}')
    xs[N] = x
    coefficients[N] = A

# проверка точности формулы на многочленах
for N in [6, 7, 8]:
    p = lambda y: y ** N
    integral = b ** (N + 1) / (N + 1) - a ** (N + 1) / (N + 1)
    approx_integral = Gaussian_integral(p, a, b, xs[N], coefficients[N])
    print(f'Погрешность интеграла x^{N} от a до b = {abs(integral - approx_integral)}')

while True:
    print('Введите значения N1, N2, N3: ')
    N1 = int(input('N1 = '))
    N2 = int(input('N2 = '))
    N3 = int(input('N3 = '))

    integral = integrate.quad(f, a, b)[0]  # точное значение интеграла
    approx_integral_1 = Gaussian_integral(f, a, b, xs[N1], coefficients[N1])
    approx_integral_2 = Gaussian_integral(f, a, b, xs[N2], coefficients[N2])
    approx_integral_3 = Gaussian_integral(f, a, b, xs[N3], coefficients[N3])

    print(f'Точное значение интеграла f(x) от {a} до {b} = {integral}')
    print(f'Приближённое значение интеграла f(x) от {a} до {b} по КФ Гаусса порядка {N1} = {approx_integral_1}')
    print(f'Погрешность = {abs(integral - approx_integral_1)}')
    print(f'Приближённое значение интеграла f(x) от {a} до {b} по КФ Гаусса порядка {N2} = {approx_integral_2}')
    print(f'Погрешность = {abs(integral - approx_integral_2)}')
    print(f'Приближённое значение интеграла f(x) от {a} до {b} по КФ Гаусса порядка {N3} = {approx_integral_3}')
    print(f'Погрешность = {abs(integral - approx_integral_3)}')

    print('Если вы хотите закончить вычисления, введите 0')
    print('Для продолжения введите любое число')
    signal = int(input())

    if signal == 0:
        break

    print('Введите пределы интегрирования: ')
    a = float(input('A = '))
    b = float(input('B = '))
