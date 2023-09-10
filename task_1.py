from math import sin, cos, sqrt


def f(x):
    return 5 * sin(2 * x) - sqrt(1 - x)


def f1(x):  # f1(x) := f'(x)
    return 10 * cos(2 * x) + 1 / (2 * sqrt(1 - x))


def f2(x):  # f2(x) := f''(x)
    return -20 * sin(2 * x) - 0.5 * (1 - x) ** (-3 / 2)


def get_roots_segments(A, B, N):
    h = (B - A) / N
    control_points = [A + i * h for i in range(0, N + 1)]
    segments = []
    for i in range(1, N + 1):
        c, d = control_points[i - 1], control_points[i]
        if f(c) * f(d) < 0:
            segments.append((c, d))
    return segments


def print_segments(segments):
    print('\nОтрезки перемены знака функции')
    for segment in segments:
        print(f'[{segment[0]}, {segment[1]}]')
    print(f'Общее количество отрезков: {len(segments)}')


def bisect(segment):
    a, b = segment[0], segment[1]
    count = 0
    x0 = a + (b - a) / 2
    while b - a >= 2 * eps:
        count += 1
        c = a + (b - a) / 2
        if f(a) * f(c) < 0:
            a, b = a, c
        else:
            a, b = c, b
    x_ = (a + b) / 2
    print('\nМетод бисекции: ')
    print(f'Начальное приближение к корню: {x0}')
    print(f'Количество шагов для достижения точности: {count}')
    print(f'Приближенное решение: {x_}')
    print(f'Длина последнего отрезка: {abs(b - a)}')
    print(f'Невязка: {abs(f(x_))}')


def secant(segment):
    a, b = segment[0], segment[1]
    x = [a, b]
    while abs(x[-1] - x[-2]) >= eps:
        x.append(x[-1] - ((x[-1] - x[-2]) * (f(x[-1]) / (f(x[-1]) - f(x[-2])))))
    print('\nМетод секущих: ')
    print(f'Начальные приближения к корню: {a, b}')
    print(f'Количество шагов для достижения точности: {len(x) - 2}')
    print(f'Приближенное решение: {x[-1]}')
    print(f'Дельта: {abs(x[-1] - x[-2])}')
    print(f'Невязка: {abs(f(x[-1]))}')


def pick_first_approximation(segment, f, f2):
    a, b = segment[0], segment[1]

    def is_convergent(x0):
        return f(x0) * f2(x0) < 0

    x0 = a + (b - a) / 2
    for i in range(1, 100):
        if is_convergent(x0):
            print(f'Начальное приближение к корню: {x0} (условие отрицательного произведения выполняется)')
            return x0
        x0 = a + (b - a) / (i % 50) if i <= 50 else b - (b - a) / (i % 50)
    print(f'Начальное приближение к корню: {x0} (условие отрицательного произведения не выполняется)')
    return x0


def run_newton_method(segment):
    print('\nМетод Ньютона')
    x = [0 for _ in range(20)]
    x[0] = pick_first_approximation(segment, f, f2)
    for k in range(1, 20):
        x[k] = x[k - 1] - f(x[k - 1]) / f1(x[k - 1])
        difference = abs(x[k] - x[k - 1])
        if difference < eps:
            print(f'Количество шагов для достижения точности: {k}')
            print(f'Приближенное решение: {x[k]}')
            print(f'Дельта (x_m - x_m-1): {difference}')
            print(f'Невязка: {abs(f(x[k]))}')
            return
    print('За 20 шагов решение заданной точности не найдено.')


def run_modify_newton_method(segment):
    print('\nМодифицированный метод Ньютона')
    x = [0 for _ in range(100)]
    x[0] = pick_first_approximation(segment, f, f2)
    for k in range(1, 100):
        x[k] = x[k - 1] - f(x[k - 1]) / f1(x[0])
        difference = abs(x[k] - x[k - 1])
        if difference < eps:
            print(f'Количество шагов для достижения точности: {k}')
            print(f'Приближенное решение: {x[k]}')
            print(f'Дельта (x_m - x_m-1): {difference}')
            print(f'Невязка: {abs(f(x[k]))}')
            return
    print('За 100 шагов решение заданной точности не найдено.')


print('''
Численные методы решения нелинейных уравнений
Отрезок: [-15, -10]
Функция: 5 * sin(2 * x) - sqrt(1 - x)
Точность: ε = 10^(-6)
''')
print('Введите границы промежутка [A, B]:')
A = float(input('A = '))
B = float(input('B = '))

N = int(input('Введите количество отрезков, на которых нужно искать корни: '))
eps = float(input('Введите точность: '))

# Отделение корней


# поиск корней
segments = get_roots_segments(A, B, N)
print_segments(segments)
bisect_roots, secant_roots = [], []
for segment in segments:
    # метод бисекции
    bisect(segment)

    # метод Ньютона
    run_newton_method(segment)

    # модифицированный метод Ньютона
    run_modify_newton_method(segment)

    # метод секущих
    secant(segment)
