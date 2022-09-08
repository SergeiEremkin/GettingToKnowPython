# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

from operator import index
from typing import List

def have_number(list_number : List, number : int) :
    have_number = False
    for str_elem in list_number:
        for elem in str_elem:
            if (elem==str(number)):
                have_number = True
                print('Такой элемент есть')
                break
    if have_number == False:
        print('Такого значения нет')        
    

have_number(['fdg5', 'dfgrd7', '8', 'fdgdf', 'trr'], 5)

