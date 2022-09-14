# 3 - В файле, содержащем фамилии студентов и их оценки,
# изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

def open_and_read(file):
    f = open(file, 'r', encoding='utf_8')
    list_student = []
    for line in f:
        list_student.append(line.strip().split())
    f.close()    
    return list_student


list_students = open_and_read('journal.txt')


def make_dict_students(list_student):
    dict_students = {}
    for student in list_student:
        for _ in range(len(student)):
            print(student[0])
            dict_students[student[0] + ' ' + student[1]] = int(student[2])
    print(dict_students)
    return dict_students


dict_students = make_dict_students(list_students)


def change_register(dict_students):
    changed_dict ={}
    new_key =''
    for key, value in dict_students.items():
        if value > 4:
            new_key = key.upper()
            changed_dict[new_key] = value
        else:
            changed_dict[key] = value    
    return changed_dict

changed_dict = change_register(dict_students)    

def write_result(dict, name):
    f = open(name, 'w', encoding='utf-8')
    for item in dict.items():
        f.write(f'{item[0]} {item[1]}\n')
    f.close()

write_result(changed_dict, 'changed_journal.txt')
print(open_and_read('journal.txt'))
make_dict_students(list_students)
print(change_register(dict_students))
