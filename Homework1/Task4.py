# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def check_range():
    while True:
        try:
            four = int(input('Введите номер четверти: '))
            if 1 <= four <= 4:
                if four == 1:
                    print('X>0, Y>0')
                    break
                elif four == 2:
                    print('X<0, Y>0')
                    break
                elif four == 3:
                    print('X<0, Y<0')
                    break
                else:
                    print('X>0, Y<0')
                    break
            else:
                print('Нужно ввести число от 1 до 4')
        except ValueError:
            print('Нужно ввести число')


check_range()
