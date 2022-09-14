from typing import List


#   1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#   N = 20 -> [2,5]
#   N = 30 -> [2, 3, 5]

def is_prime(N: int):
    list_det_of_n = []
    for i in range(2, N+1):
        if i > 1 and (i % 2 != 0 or i == 2) and (
                i % 3 != 0 or i == 3) and N % i == 0:
            list_det_of_n.append(i)
    return list_det_of_n


print(is_prime(20))
print(is_prime(30))
