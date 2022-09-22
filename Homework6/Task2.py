# 2- Найти сумму чисел списка стоящих на нечетной позиции

numbers = [2, 10, 5, 9, 3]
odd_elements = [numbers[i] for i in range(len(numbers)) if i % 2 ==1]
print (sum(odd_elements))