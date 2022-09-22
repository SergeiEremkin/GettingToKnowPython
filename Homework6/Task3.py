# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

# 5-Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21



from math import sqrt
from check import check_number_without_change



input_coordinates = check_number_without_change('Введите  координаты x и y для точек а и b точек в пространстве через пробел(4 оординаты): ')
coordinates = [int(x) for x in input_coordinates.split(' ')]
print(input_coordinates) 
check_range_points = lambda ax, ay, bx, by: (round((sqrt(int((bx - ax))**2+int((ay - by))**2)), 2))
print(check_range_points(coordinates[0], coordinates[1], coordinates[2], coordinates[3]))

