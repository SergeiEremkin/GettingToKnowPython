# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from typing import List

'''Заполнил список 1 и 0 в обратном порядке'''


def fill_list_binary_numbers(number: int) -> List[int]:
    binary_list = []
    while number != 0:
        rest = number % 2
        binary_list.append(rest)
        number //= 2
    return binary_list


def convert_to_binary(number: int) -> int:
    result = ''
    try:
        binary_list = fill_list_binary_numbers(number)
        for list in binary_list[::-1]:
            result += str(list)
        result = int(result)
    except TypeError:
        result ='Введено не число, операция не выполнима'
    return result


print(convert_to_binary(61))
print(convert_to_binary('df'))
