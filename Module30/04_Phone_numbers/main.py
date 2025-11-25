import re

def check_numbers(input_numbers: list[str]) -> None:
    """
    Функция фильтрует правильные номера от неправильных

    :param input_numbers: Список входных номеров
    :return: None
    """
    words = ["первый", "второй", "третий", "четвёртый", "пятый", "шестой", "седьмой", "восьмой", "девятый", "десятый"]

    for i, number in enumerate(input_numbers):
        if re.fullmatch(r'[89]\d{9}', number):
            status = 'все в порядке'
        else:
            status = 'не подходит'
        if i < len(words):
            print(f'{words[i]} номер: {status}')


list_numbers = ['9999999999', '999999-999', '99999x9999']
check_numbers(list_numbers)




