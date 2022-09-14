from typing import List


def write_string_in_file(word_name, filename):
    file = open(filename, 'w', encoding='utf-8')
    file.write(word_name)
    file.close()

def check_list_for_int(list_elements: List[int]) -> bool:
    '''Метод проверяет все ли элементы списка - числа или нет. Возвращает bool.'''
    return all(isinstance(x, int) for x in list_elements)

def check_list_for_float(list_elements: List[int]) -> bool:
    '''Метод проверяет все ли элементы списка - числа или нет. Возвращает bool.'''
    return all(isinstance(x, float) for x in list_elements)        