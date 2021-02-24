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
record = 100
answer = "y"
while answer == "y":
    gen = random.randint(1, 100)
    tries = 1
    print()  # Отступ верхней строки
    print('Сгенерировано случайное число от 1 до 100. Попробуйте угадать!')
    num = None
    while gen != num:
        try:
            num = int(input('Введите число: '))
        except ValueError:
            exit('Всё сломалось, введено не число или не целое число.')
        if gen < num:
            print('Много!')
            tries += 1
        elif gen > num:
            print('Мало!')
            tries += 1
        else:
            print(' Вы угадали! Попыток:', tries)
    if record > tries:
        record = tries
        print('Новый рекорд! Попыток:', record)
    answer = input("Продолжить? y/n ")
    if answer == "n":
        print('Пока!')