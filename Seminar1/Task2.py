# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# 3. Пользователь вводит время в минутах и расстояние в километрах. Найдите скорость в м/c..

def show_numbers(N):
    N = abs(N)
    print(*[i for i in range(N*-1, N+1)])


def first_number_float(fl):
    if isinstance(fl, float):
        print(int((round(fl, 1)*10) % 10))
    else:
        print('Нет')


def find_speed():
    time = int(input('Введите время в минутах: '))
    distance = int(input('Введите расстояние в километрах: '))
    print(f'Скорость = {round((distance*1000)/(time*60), 2)} м/с')


show_numbers(-5)
first_number_float(5.01)
find_speed()
