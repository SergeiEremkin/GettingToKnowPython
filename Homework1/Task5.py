from math import sqrt

# 5-Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def check_range_points(ax, ay, bx, by):
  
    return print(round((sqrt(int((bx - ax))**2+int((ay - by))**2)), 2))


check_range_points(2, 4, 4, 5)
check_range_points(0, 0, 0, 0)
check_range_points(433, 732, 323, 3233)
