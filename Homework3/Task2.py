# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from typing import List
from check import check_list_for_int



def multiply_of_numbers(list_numbers: List) -> None:
    """ - делим список на 2 половины
    - перемножаем с помошью цикла for 2 половины. Первую половину берем с начала, а вторую с конца
    - если сумма элементов нечетная, то прибавляем элемент, который не вошел в интервалы в список
    """
    
    if check_list_for_int(list_numbers):
            result_list = []
            half_len = len(list_numbers)//2 + len(list_numbers)%2
            for i in range(half_len):
                result_list.append(list_numbers[i]*list_numbers[-1-i])
            print(result_list)
    else:
        print('Нужен список чисел')


multiply_of_numbers([2, 3, 4, 5, 6])
multiply_of_numbers([2, 3, 5, 6])
multiply_of_numbers(['d', 'sdsd'])
