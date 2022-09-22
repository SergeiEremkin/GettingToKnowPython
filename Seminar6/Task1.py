# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок


string_numbers = '-22+2'


def operations_with_number(string_numbers):
    operations = ['+', '-', '/', '*']
    list_operation = []
    number = ''
    list_numbers = []
    for symbol in string_numbers + ' ':
        if symbol.isdigit():
            number += symbol
            continue
        elif number:
            list_numbers.append(int(number))
            number = ''
            if symbol[0] == operations[1]:
                list_numbers[0] *= -1
        print(list_numbers)
        if symbol in operations:
            list_operation.append(symbol)
        
        print(list_operation)

        # if string_numbers.index(operations[1]):
        #    string_numbers[string_numbers.index(operations[1])+1]
        #    if string_numbers[string_numbers.index(operations[1])+1].isdigit():
        #         while
        #         number+=string_numbers[string_numbers.index(operations[1])+1]


operations_with_number(string_numbers)
