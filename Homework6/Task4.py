# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1



from operator import index


strings = ["asd",'qwe', "zxc",'qwe', "ertqwe"] #ищем: "qwe"
search_string = "qwe"

try:
    second_element = [x for x in range(len(strings))[strings.index(search_string)+1::] if strings[x] == search_string]
    if second_element:
        print (f'Второе вхождение элемента под индексом: {second_element[0]}')
    else:
        print('Данного элемента нет')
except ValueError:
    print('Такого элемента нет в списке')



       