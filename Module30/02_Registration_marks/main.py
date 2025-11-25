import re
from typing import List, Tuple

def find_numbers(input_numbers: str) -> Tuple[List[str],List[str]]:
    """
    Фильтрует из перечня номеров на частные номера и номера такси

    :param input_numbers: Перечень номеров
    :return: Два списка с отфильтрованными номерами
    """
    private_num = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', input_numbers)
    taxi_num = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', input_numbers)
    return private_num, taxi_num

registration_marks = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_num, taxi_num = find_numbers(registration_marks)

print(f'Список частных автомобилей:', private_num)
print('Список номеров такси:', taxi_num)