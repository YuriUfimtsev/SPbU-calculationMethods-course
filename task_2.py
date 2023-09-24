import polynomial as pol
from math import exp


def f(x_):
    return 1 - exp(-x_) + x_ ** 2


def product(l_):
    result = pol.Polynomial(1)
    for i in range(len(l_)):
        result *= l_[i]
    return result


def w(n_, z_):
    return product([pol.Polynomial(1, -z_[k]) for k in range(n_ + 1)])


def l(k, n_, z_):
    return w(n_, z_) // (pol.Polynomial(1, -z_[k]) * w(n_, z_).derivative.calculate(z_[k]))


def L(n_, z_):
    result = pol.Polynomial(0)
    for k in range(n_ + 1):
        result += pol.Polynomial(f(z_[k])) * l(k, n_, z_)
    return result


def Lagrange(n_, z_, x_):
    return L(n_, z_).calculate(x_)


print('Задача алгебраического интерполирования')
print('Вариант 9')

points_count = int(input('Введите количество узлов интерполяции: m + 1 = '))
print('Введите отрезок, на котором нужно интерполировать функцию: ')
A = float(input('A = '))
B = float(input('B = '))
z = [A + i * (B - A) / points_count for i in range(points_count)] # узлы интерполяции
y = [f(z[i]) for i in range(points_count)]
print('Таблица значений функции: ')
for j in range(points_count):
    print(f'f({z[j]}) = {y[j]}')

x = float(input('Введите точку интерполирования: x = '))
n = int(input(f'Введите степень интерполяционного многочлена n (n < {points_count}): '))

# сортируем узлы интерполирования по расстоянию от точки x
z1 = [(abs(z[i] - x), z[i]) for i in range(points_count)]
z1.sort()
z = list(map(lambda p: p[1], z1))
y = [f(z[i]) for i in range(points_count)]
for j in range(points_count):
    print(f'f({z[j]}) = {y[j]}')

approximate_value = Lagrange(n, z, x)

print(f'Значение интерполяционного многочлена P(x) = {approximate_value}')
print(f'Погрешность ef(x) = {abs(f(x) - approximate_value)}')









