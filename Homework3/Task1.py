# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from typing import List

'''Метод проверяет все ли элементы списка - числа или нет. Возвращает bool.'''


def check_list_for_int(list_element: List[int]) -> bool:
    return all(isinstance(x, int) for x in list_element)


"""Если после проверки в списке все числа, то метод складывает элементы с нечетными индексами.
Если нет то обрабатывает exception - TypeError.
"""


def sum_odd(list_element: List[int])-> None:
    sum_elements = 0
    try:
        if check_list_for_int:
            for i in range(len(list_element)):
                if i % 2 == 1:
                    sum_elements += list_element[i]
            print(
                f'Сумма элементов списка, состоящих из нечетных индексов = {sum_elements}')
    except TypeError:
        print('Нужен список чисел')


sum_odd([2, 10, 5, 9, 3])
sum_odd([1, 'sds', 4])
sum_odd([1])
