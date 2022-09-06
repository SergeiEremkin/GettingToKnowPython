# ;  Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# ; Не используйте функцию math.factorial.

# ; Пример:
# ; - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def res_fact(N):
    factorial = 1
    list_factorial = []
    for i in range(2, N+1):
        list_factorial.append(factorial)
        factorial *= i
    print(list_factorial)


res_fact(5)
res_fact(96)
