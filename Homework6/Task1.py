# 1- Определить, присутствует ли в заданном списке строк, некоторое число
     

number = 5 
have_number = [l for x in ['fdg5', 'dfgrd', '8', 'fdgdf', 'trr'] for l in x if l == str(number)]
print(have_number)
result = lambda have_number:'Такой элемент есть в списке' if have_number else 'Такого элемента нет'
print(result(have_number))


