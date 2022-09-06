# 2.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами
# элементы не могут повторятся

def sum_min_max(list_elem):
    index_max = list_elem.index(max(list_elem))
    index_min = list_elem.index(min(list_elem))
    
    if(index_min<index_max):
        list_result = list_elem[index_min:index_max+1]
    else:
        list_result = list_elem[index_max:index_min+1]
    print(sum(list_result))  
    
    #print(f'Сумма элементов массива = {sum(new_list)}')


sum_min_max([2,3,6,7,45])
sum_min_max([100,3,6,7,1])
