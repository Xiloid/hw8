"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.
    Напишите несколько тестов для функции.
    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"
"""
text = "hi world, hi python. i am very cool but i am still learning."


def main():
    print_list = frequent_word(text)
    print('Список наиболее часто встречающихся слов по алфавиту:')
    print(print_list)


def frequent_word(text):
    tmp_dict = {}
    for a in text.split(' '):
        for b in a.split():
            tmp_dict[b] = tmp_dict.get(b, 0) + 1
    most_word = tmp_dict[max(tmp_dict, key=lambda i: tmp_dict[i])]
    out_list = (sorted([j for j in tmp_dict if tmp_dict[j] == most_word]))
    return out_list[0]


assert frequent_word(text) == 'am'


if __name__ == "__main__":
    main()
