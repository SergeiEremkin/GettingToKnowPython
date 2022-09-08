# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

def check_double(list_elements, search_string):
    count = 0
    for i in range(len(list_elements)):
        if search_string == list_elements[i]:
            count+=1
        if count == 2:    
            print(f' {i}')
            break

#check_double(["qwe", "asd", "zxc", "qwe", "ertqwe"], 'qwe')
       
