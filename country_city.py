"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.
    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""
'''
data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
}'''


def main():
    city = input(': ')
    data = {'Ukraine': ['Kiev', 'Kharkiv', 'Odesa', 'Dnipro']}
    for item in data.values():
#        print((item[2]))
        if item[0] == city:
            print(item[0])
            print('ok')
        else:
            print(item)
            print('ooops')
#    print(data.values())

'''    in_city = input('Город? ')
#    get_country(in_city)
    for item in data.values():
        if in_city == item:
            print(data.keys(item))
#        print(item)
'''
'''
def get_country(city):
    for x in data.keys():  # Перебор всех ключей словаря
        if 
        for i in range(len(data[k])):  # Перебор всех подмассивов по ключу
            print(k)
#            for j in range(3, len(data[k][i])):  # Перебор элементов подмассива, содержащих нужный текст
#                print(data[k][i][j][0])  # Вывод результата


def groupping_data(data):
    pass

'''
if __name__ == "__main__":
    main()