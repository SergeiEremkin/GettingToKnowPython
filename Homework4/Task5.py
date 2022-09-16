# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

from check import write_string_in_file
from check import read_string_from_file

data = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
filename = 'uncompressed.txt'
filename2 = 'compressedfile.txt'

write_string_in_file(data, filename)


def encode(data):
    encoding = []
    count = 1
    char = data[0]
    for i in range(1, len(data)):
        if data[i] == char:
            count += 1
        else:
            encoding.append([count, char])
            char = data[i]
            count = 1
    encoding.append([char, count])
    return encoding


encoded_list = encode(data)


def encode_to_string(encoded_list):
    compressed = ''
    for i in range(0, len(encoded_list)):
        for j in encoded_list[i]:
            compressed += str(j)
    return compressed


encoded_string = encode_to_string(encoded_list)

write_string_in_file(encoded_string, filename2)

encoded_string = read_string_from_file(filename)


def decode(encoded_string):
    decompressed = ''
    for i in range(0, len(encoded_string)):
        if encoded_string[i].isalpha() or encoded_string[i].isspace() == True:
            decompressed += encoded_string[i]
    return decompressed


print(decode(encoded_string))
