# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4                 2 X<0, Y>0   1 (X>0,Y>0)
# - x=2; y=4-> 1                     3 X<0, Y<0   4 (X>0, Y<0)
# - x=-34; y=-30 -> 3

def check_plane_number(X, Y):
    if X == 0 and Y == 0:
        print('Точка находится в начале координат')
    else:
        if X > 0 and Y > 0:
            print('Точка находится в 1 четверти')
        elif X < 0 and Y > 0:
            print('Точка находится во 2 четверти')
        elif X < 0 and Y < 0:
            print('Точка находится в 3 четверти')
        elif X > 0 and Y < 0:
            print('Точка находится в 4 четверти')
        else:
            if X == 0 and Y != 0:
                print('Точка лежит на оси X')
            else:
                print('Точка лежит на оси Y')


check_plane_number(1, 0)
check_plane_number(0, 1)
check_plane_number(0, 0)
check_plane_number(1, 1)
check_plane_number(-1, 1)
check_plane_number(-1, -1)
check_plane_number(1, -1)
