# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def check_polindrom(number):
    start_number = number
    count = 0
    while True:
        number = str(number)
        if str(number) == str(number)[::-1]:
            print(
                f'{number} - Это палиндром от {start_number}, преобразование произошло {count} раз')
            break
        else:
            reverse_number = str(number)[::-1]
            number = int(number) + int(reverse_number)
            count += 1


check_polindrom(12)
check_polindrom(55)
check_polindrom(89)
