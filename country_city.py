"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.
    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""

data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
}


def main():
    city = input('Введите название города: ')
    city_result = get_country(city)
    print(f'Страна, которой принадлежит город {city}: {city_result}')
    print()
    final_list = groupping_data(data)
    print('Отформатированный список согласно условия:')
    print(groupping_data(data))


def get_country(city):
    for key, value in data.items():
        for j in value:
            if j == city:
                return key


def groupping_data(data):
    list = []
    for key, val in data.items():
        a_country = {'country': key}
        b_capital = {'capital': val[0]}
        c_cities = {'cities': val[1:4]}
        data_final = a_country | b_capital | c_cities
        list.append(data_final)
    return list


if __name__ == "__main__":
    main()
