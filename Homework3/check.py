from typing import List


def check_list_for_int(list_elements: List[int]) -> bool:
    '''Метод проверяет все ли элементы списка - числа или нет. Возвращает bool.'''
    return all(isinstance(x, int) for x in list_elements)

def check_list_for_float(list_elements: List[int]) -> bool:
    '''Метод проверяет все ли элементы списка - числа или нет. Возвращает bool.'''
    return all(isinstance(x, float) for x in list_elements)    