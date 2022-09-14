# 1 - Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

from posixpath import split


numbers_nums = '2 3 4 5 7'


def min_max_nums(numbers):
    string_numbers = numbers.split(' ')
    print(
        f'Максимальное число  = {max(string_numbers)}, минимальное число {min(string_numbers)}')


min_max_nums(numbers_nums)
