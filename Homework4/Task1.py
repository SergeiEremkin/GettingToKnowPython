from typing import List


#   1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#   N = 20 -> [2,5]
#   N = 30 -> [2, 3, 5]

def take_divisors(N: int):
    list_det_of_n = []
    for i in range(2, N+1):
        if N % i == 0:
            count = 1
            for j in range(2, i//2+1):
                if i % j == 0:
                    count = 0
                    break
            if count == 1:
                list_det_of_n.append(i)
    return list_det_of_n


print(take_divisors(20))
print(take_divisors(30))
print(take_divisors(650))
