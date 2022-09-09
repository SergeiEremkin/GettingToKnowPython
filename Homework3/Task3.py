# 3-Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.01] => 0.19 или 19
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91


from posixpath import split
from typing import List
"""- Проверяю максимальное кол-во цифр в числе, для того 
    чтобы понять на сколько округлять результат при подсчете.
"""


def max_lenght_element(list_float: List[float]) -> int:
    counter = 0
    max_count = 0
    string_float = str(list_float)
    list_string_float = string_float.split(',')
    for float in list_string_float:
        for char in float:
            counter += 1
            if max_count < counter:
                max_count = counter
                counter = 0
    return max_count


'''Считаю разницу, перед этим убрав целую часть'''


def float_difference_between_the_numbers(list_float: List[float]) -> None:
    round_point = max_lenght_element(list_float)
    result_list = []
    for elem in list_float:
        result_list.append(elem - int(elem))
    max_element = max(result_list)
    min_element = min(result_list)
    print(round((max_element - min_element), round_point))


float_difference_between_the_numbers([1.16, 1.2, 3.1, 5.17, 10.01])
float_difference_between_the_numbers([4.07, 5.1, 8.2444, 6.98])
