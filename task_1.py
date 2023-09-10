from math import sin, cos, sqrt


def f(x):
    return 5 * sin(2 * x) - sqrt(1 - x)


def f1(x):  # f1(x) := f'(x)
    return 10 * cos(2 * x) + 1 / (2 * sqrt(1 - x))


def f2(x):  # f2(x) := f''(x)
    return -20 * sin(2 * x) - 0.5 * (1 - x) ** (-3 / 2)


print('Введите границы промежутка [A, B]:')
A = float(input('A = '))
B = float(input('B = '))

N = int(input('Введите количество отрезков, на которых нужно искать корни: '))
eps = float(input('Введите точность: '))


# Отделение корней
def get_roots_segments(A, B, N):
    h = (B - A) / N
    control_points = [A + i * h for i in range(0, N + 1)]
    segments = []
    for i in range(1, N + 1):
        c, d = control_points[i - 1], control_points[i]
        if f(c) * f(d) < 0:
            segments.append((c, d))
    return segments


# поиск корней
segments = get_roots_segments(A, B, N)
bisect_roots, secant_roots = [], []
for segment in segments:
    a, b = segment[0], segment[1]

    # метод бисекции
    # print('Метод бисекции: ')
    while b - a >= 2 * eps:
        c = a + (b - a) / 2
        if f(a) * f(c) < 0:
            a, b = a, c
        else:
            a, b = c, b
    x_ = (a + b) / 2
    bisect_roots.append(x_)

    # метод Ньютона

    # модифицированный метод Ньютона

    # метод секущих
    # print('Метод секущих: ')
    a, b = segment[0], segment[1]
    x = [a + (b - a) / 2, a + (b - a) / 2]
    while abs(x[-1] - x[-2]) >= eps:
        x.append(x[-1] - f(x[-1]) / (f(x[-1]) - f(x[-2])))
    # print(x[-1])
    secant_roots.append(x[-1])

print('Метод бисекции: ')
for i in bisect_roots:
    print(i)
print()
print('Метод секущих: ')
for i in secant_roots:
    print(i)
