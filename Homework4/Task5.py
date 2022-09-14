# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

from check import write_string_in_file

data = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
filename = 'uncompressed.txt'
filename2 = 'compressedfile.txt'

write_string_in_file(data, filename)

def encode(data):
    encoding = ""
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + data[i]
        i = i + 1
    return encoding

write_string_in_file(data, filename)
compressed = encode(data)
write_string_in_file(compressed, filename2)

