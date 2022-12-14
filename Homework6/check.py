from typing import List


def write_string_in_file(word_name, filename):
    file = open(filename, 'w', encoding='utf-8')
    file.write(word_name)
    file.close()

def read_string_from_file(filename) :
    file = open(filename, 'r', encoding='utf-8')
    string_file = file.readline()
    file.close()
    return string_file    

def check_list_for_int(list_elements: List[int]) -> bool:
    '''Метод проверяет все ли элементы списка - числа или нет. Возвращает bool.'''
    return all(isinstance(x, int) for x in list_elements)

def check_list_for_float(list_elements: List[int]) -> bool:
    '''Метод проверяет все ли элементы списка - числа или нет. Возвращает bool.'''
    return all(isinstance(x, float) for x in list_elements)        

def check_number(message):
    while True:
        try:
            user_input = input(message)
            if user_input.isdigit():
                user_input = int(user_input)
                break
        except ValueError:
            print('Нужно ввеcти число')
    return user_input    

def check_number_without_change(message):
    while True:
        try:
            user_input = input(message)
            if user_input.isdigit():
                break
        except ValueError:
            print('Нужно ввеcти число')
    return user_input    