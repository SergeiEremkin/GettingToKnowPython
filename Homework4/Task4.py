# 4- Шифр Цезаря - это способ шифрования,
# где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо,
# "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


shift = -2
letter = 'привет'
filename = 'encoded.txt'


def encode_letter(letter, shift):
    dictionary = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    encoded = ''
    for pos in range(len(letter)):
        index = dictionary.index(letter[pos])
        index = index + shift + len(dictionary) % len(dictionary)
        encoded += dictionary[index]
    return encoded


def write_string_in_file(word_name, filename):
    file = open(filename, 'w', encoding='utf-8')
    file.write(word_name)
    file.close()


def read_string_from_file():
    file = open('encoded.txt', 'r', encoding='utf-8')
    encode = file.readline()
    file.close()
    return encode


def decode_letter(shift):
    answer = input('Введите ключ: ')
    right_key = '1234'
    encode = read_string_from_file()

    decoded = encode_letter(encode, -shift)

    if answer == right_key:
        print(f'Зашифрованный текст: {encode}, расшифрованный: {decoded}')
    else:
        print('Пароль неверный')


encoded = encode_letter(letter, shift)
write_string_in_file(encoded, filename)
decode_letter(shift)
