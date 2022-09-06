# 3.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.

def max_10 (list_elem):
    count = 0
    max_elem = max(list_elem)
    number_x10 = max_elem * 0.1
    for i in list_elem:
        if(i >= max_elem - number_x10) and i != max_elem:
            count+=1
            print(count) 
        else:
            print("Таких элементов нет")  

max_10([1,2,3,4,56,78])              