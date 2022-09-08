# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



from typing import List


def check_list_for_int(list_element: List[int]) -> bool:
    return all(isinstance(x, int) for x in list_element)
   

def sum_odd(list_element: List[int]) -> int:
    sum_elements = 0
    try:
        if check_list_for_int:
            for i in range(len(list_element)):
                if i % 2 == 1:
                    sum_elements += list_element[i]
    except:
        sum_elements ='нужен список чисел'
    else:
        print('элементов с нечетным индесом нет в списке')             
    return sum_elements


print(sum_odd([2, 10, 5, 9, 3]))
print(sum_odd([1,'sds',4]))
print(sum_odd([1]))

# if list_element == [] or list_element == [1]:
#             sum_elements = str('В массиве нет элементов с нечетными индексами')