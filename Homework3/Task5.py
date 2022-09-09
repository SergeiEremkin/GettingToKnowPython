# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/yWbkX.)
# Решение оформлять в виде функций
# По возможности добавляйте docstring

# Fn = F(n+2)−F(n+1) нега
# F_{n}=F_{n-1}+F_{n-2}} обычный

"""
Если n больше нуля, то идет по первому if, если < 0 то по второму. Первые 2 элемента нам известны,
    мы сразу внесли их в список x, добавляем элементы по формуле со 2 индекса.
"""


def fibo(n):
    if n >= 0:
        idx = range(n+1)
        x = [0, 1]
        for k in idx[2:]:
            x.append(x[k-1] + x[k-2])
        return x[n]
    else:
        n = -(n-1)
        idx = range(n+1)
        x = [1, 0]
        for k in idx[2:]:
            x.append(x[k-2] - x[k-1])
        x.reverse()
    return x[0]


'''вводим числовой диапозон'''


def show_fib_in_range(min, max):
    for i in range(min, max+1):
        print(fibo(i), end=' ')


show_fib_in_range(-8, 8)
