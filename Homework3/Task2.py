# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from typing import List

'''Метод проверяет все ли элементы списка - числа или нет. Возвращает bool.'''


def check_list_for_int(list_element: List[int]) -> bool:
    return all(isinstance(x, int) for x in list_element)


""" - делим список на 2 половины
    - перемножаем с помошью цикла for 2 половины. Первую половину берем с начала, а вторую с конца
    - если сумма элементов нечетная, то прибавляем элемент, который не вошел в интервалы в список
"""


def multiply_of_numbers(list_numbers: List) -> None:
    try:
        if check_list_for_int:
            result_list = []
            half_len = len(list_numbers)//2
            first_half = list_numbers[:half_len]
            second_half = list_numbers[half_len:]
            for i in range(len(first_half)):
                result_list.append(first_half[i]*second_half[-1-i])
            if len(list_numbers) % 2 == 1:
                result_list.append(list_numbers[half_len]**2)
        print(result_list)
    except TypeError:
        print('Нужен список чисел')


multiply_of_numbers([2, 3, 4, 5, 6])
multiply_of_numbers([2, 3, 5, 6])
multiply_of_numbers(['d', 'sdsd'])
