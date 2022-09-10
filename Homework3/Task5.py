# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/yWbkX.)
# Решение оформлять в виде функций
# По возможности добавляйте docstring

# Fn = F(number+2)−F(number+1) нега
# F_{number}=F_{number-1}+F_{number-2}} обычный

from typing import List


def fibo(number: int) -> List:
    """
    Если number больше нуля, то идет по первому if, если < 0? . Первые 2 элемента нам известны,
    мы сразу внесли их в список fibo_list, добавляем элементы по формуле со 2 индекса.
    """
    if number >= 0:
        idx = range(number+1)
        fibo_list = [0, 1]
        for k in idx[2:]:
            fibo_list.append(fibo_list[k-1] + fibo_list[k-2])
    else:
        number = -(number-1)
        idx = range(number+1)
        fibo_list = [1, 0]
        for k in idx[2:]:
            fibo_list.append(fibo_list[k-2] - fibo_list[k-1])
        fibo_list.reverse()
    return fibo_list


def make_list_of_negafibo(number: int) -> List:
    """
    Метод принимает на вход число, берем его по модулю. И далее делаем отдельно 2 листа, 1 на отрицательное число,
    второй на положительное и потом добавляем его в результирующий - list_negafibo
    """
    list_negafibo = []
    number = abs(number)
    plus_fibo = fibo(number)[2:]
    minus_fibo = fibo(-number)
    for num in minus_fibo:
        list_negafibo.append(num)
    for num in plus_fibo:
        list_negafibo.append(num)
    return list_negafibo


print(make_list_of_negafibo(8))
print(make_list_of_negafibo(-8))
