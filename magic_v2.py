"""
    Реализуйте игру Magic (hw3/magic.py) с некоторыми дополнениями.
    1. При запуске, программа спрашивает имя игрока.
    2. В словаре player_data хранить данные игрока и актуализировать их после
    каждой сыгранной игры. Оперировать такими данными:
        name - имя игрока
        games - общее количество сыграных игр
        record - рекордное количество попыток (минимальное)
        avg_attempts - среднее количество попыток за игру
    3. При выходе из программы данные игрока записывать в файл (txt либо json).
    **4. При запуске программы, после ввода имени пользователем, читать файл,
    если данные об игроке есть в файле то загружать их в player_data.
"""
import random
from pathlib import Path


def main():
    record = 1000
    answer = "y"
    summ = count = avr = 0
    gamer_name = input('Введите имя игрока: ')
    while answer == "y":
        gen = random.randint(1, 100)
        num = None
        print('Сгенерировано случайное число от 1 до 100. Попробуйте угадать!')
        tries = tries_amount(num, gen)
        summ += tries
        count += 1
        if record > tries:
            record = tries
            print('Новый рекорд! Попыток: ', record)
        avr = summ // count
        player_data = {'name': gamer_name, 'games': count, 'avg_attempts': avr, 'record': record}
        answer = input("Продолжить? y/n ")
        if answer == "n":
            file_record(player_data)
            print('Bye!')


def tries_amount(num, gen):
    tries = 1
    while gen != num:
        num = int(input('Введите число: '))
        if gen < num:
            print('Много!')
            tries += 1
        elif gen > num:
            print('Мало!')
            tries += 1
        else:
            print('Вы угадали! Попыток: ', tries)
    return tries


def file_record(player_data):
    path = Path('gamers.txt').resolve()
    with open(path, 'a+') as f:
        f.write(str(player_data) + '\n')
        f.close()


if __name__ == "__main__":
    main()
