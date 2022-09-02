# 2-Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#  Предикату можно заменить на понятие "бит".
# ¬ - отрицание (унарная операция), not
# ⋀ - конъюнкция, логическое умножение (бинарная), and
# ⋁ - дизъюнкция, логическое сложение (бинарная), or

def check_true():
    for X in (True, False):
        for Y in (True, False):
            for Z in (True, False):
                if not (X or Y or Z) == (not X and not Y and not Z):
                    print(
                        f'| {X} | {Y} | {Z} | {not(X or Y or Z) == (not X and not Y and not Z)} |')
                    print('-------------------------------')
                else:
                    print(
                        f'| {X} | {Y} | {Z} | {not(X or Y or Z) == (not X and not Y and not Z)} |')
                    print('-------------------------------')


check_true()
