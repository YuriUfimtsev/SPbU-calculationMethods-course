

print('Задача приближённого вычисления определённого интеграла с помощью квадратурных формул Гаусса')
print('Вариант 9')

print('Введите количество узлов интерполяции:')
N = int(input('N = '))
print('Введите узлы интерполяции через пробел:')
x = [int(i) for i in input().split()]
for i in range(N):
    for j in range(i + 1, N):
        if i != j and x[i] == x[j]:
            print('Вы ввели неправильный набор узлов интерполяции: два узла совпадают')
            break
else:
    # находим моменты мю

    # составляем и решаем СЛАУ
