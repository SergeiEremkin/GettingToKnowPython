# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11


def sum_float_number(float_number):
    try:
        float_number = abs(float(float_number))
        list_float_number = str(float_number).split('.')
        f_string = []
        result = 0
        for char in list_float_number:
            f_string += char
        for num in f_string:
            num = int(num)
            result += num
        print(result)
    except ValueError:
        print("Нужно ввести вещественное число")


sum_float_number('ывывэ')
sum_float_number(2)
sum_float_number(232323.2232323)
sum_float_number(-232323.2232323)
