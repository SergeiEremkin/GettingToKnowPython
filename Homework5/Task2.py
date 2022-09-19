# 2 - Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите).
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

import random


def check_number(message):
    while True:
        try:
            user_input = input(message)
            if user_input.isdigit():
                user_input = int(user_input)
                break
        except ValueError:
            print('Нужно ввеcти число')
    return user_input


def user_interface():
    print(50*'\n')
    print('Добро пожаловать в игру "Конфета". Цель игры, чтобы ваш противник взял последнюю конфету.\n')
    total_count = check_number('Введите кол-во конфет в куче: ')
    while True:
        turn = check_number(
            'Введите кол-во конфет, которое можно забрать за ход.\n(Оно должно быть меньше общего колличества конфет в куче): ')
        if turn < total_count:
            break
    while True:
        user_choise = check_number(
            'Если вы хотите играть против человека, напишите - 1\nЕсли вы хотите играть против компьютера, напишите - 2\n')
        print('Кто будет ходит первым ходить? Будет брошен случайный жребий.\n')
        if user_choise == 1:
            game_logic_pvp(total_count, turn)
            break
        elif user_choise == 2:
            game_logic_pve(total_count, turn)
            break
        else:
            print('Введите 1 или 2')
    


def player_turn(total_count, turn):
    while True:
        player_input = check_number(
            f'Введите число в диапазоне от 1 до {turn}: ')
        print('\n')
        if player_input <= turn and player_input > 0:
            break
    total_count -= player_input
    return total_count


def computer_turn(total_count, turn):
    if total_count < turn:
        turn = turn - (turn - total_count)-1
    total_count -= turn
    return total_count


def game_logic_pvp(total_count, turn):
    is_turn = random.randint(1, 2)
    while total_count > 1:
        if is_turn == 1:
            print(f'Ход ПЕРВОГО игрока.\nВ куче {total_count} конфет\n')
            total_count = player_turn(total_count, turn)
            if total_count > 0:
                is_turn = 2
        if is_turn == 2:
            print(f'Ход ВТОРОГО игрока.\nВ куче {total_count} конфет\n')
            total_count = player_turn(total_count, turn)
            if total_count > 0:
                is_turn = 1
        if total_count < turn:
            turn = turn - (turn - total_count)
    print(f'(В куче осталось {total_count} конфет)')
    if is_turn == 1:
        print('Игрок №1 вы проиграли. Последний ход остался за вами')
    if is_turn == 2:
        print('Игрок №2 вы проиграли. Последний ход остался за вами')


def game_logic_pve(total_count, turn):
    is_turn = random.randint(1, 2)
    while total_count > 1:
        if is_turn == 1:
            print(f'Ход игрока.\nВ куче {total_count} конфет\n')
            total_count = player_turn(total_count, turn)
            if total_count > 0:
                is_turn = 2
        if is_turn == 2:
            print(f'Ход компьютера.\nВ куче {total_count} конфет\n')
            total_count = computer_turn(total_count, turn)
            if total_count > 0:
                is_turn = 1
        if total_count < turn:
            turn = turn - (turn - total_count)
    print(f'В куче осталось {total_count} конфет')

    if is_turn == 1:
        print('Игрок №1 вы проиграли. Последний ход остался за вами')
    if is_turn == 2:
        print('Компьютер проиграл. Последний ход остался за ним')


user_interface()
