# 3-Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.01] => 0.19 или 19
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

from typing import List
from check import check_list_for_float


def max_lenght_element(list_float: List[float]) -> int:
    """
    Проверяю максимальное кол-во цифр в правой части, для того 
    чтобы понять на какое число округлять результат при подсчете.
    """
    max_count = 0
    if check_list_for_float(list_float):
        element_of_right_side = []
        for float in list_float:
            float = str(float).split('.')
            for i in range(len(float)-1):
                element_of_right_side.append(float[i+1])
        for element in element_of_right_side:
            if max_count < len(element):
                max_count = len(element)
    return max_count


def float_difference_between_the_numbers(list_float: List[float]) -> None:
    '''Считаю разницу, перед этим убрав целую часть'''
    round_point = max_lenght_element(list_float)
    result_list = []
    for elem in list_float:
        result_list.append(elem - int(elem))
    max_element = max(result_list)
    min_element = min(result_list)
    print(round((max_element - min_element), round_point))


float_difference_between_the_numbers([1.16, 1.2, 3.1, 5.17, 10.01])
float_difference_between_the_numbers([4.07, 5.1, 8.2444, 6.98])
