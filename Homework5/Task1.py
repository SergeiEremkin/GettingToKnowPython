# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

text ='абвгдейка - это передача'
text = text.split()
string_text = " ".join(map(str,[t for t in text if 'абв' not in t]))
print(string_text)




