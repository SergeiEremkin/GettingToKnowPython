# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from typing import List

list_number = [2, 3, 4, 5, 6]
list_result = [list_number[i]* list_number[-1-i] for i in range(len(list_number)//2 + len(list_number)%2)]
print(list_result)