
# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)
import time


def random_without_random(minimum, maximum):
       random_time = str(time.perf_counter())
       rnd = float(random_time [::-1][:3:])/1000
       print(rnd)
       return int(minimum + rnd * (maximum-minimum))
       
print(random_without_random(1,50))



