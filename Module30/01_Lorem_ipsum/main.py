import re
from typing import List

def find_words(input_text :str) -> List[str]:
    """
    Извлекает из текста все слова, состоящие ровно из четырех букв.
    Использует регулярное выражение с границами слов.
    :param input_text: Входной текст
    :return: Список слов из четырех букв
    """
    four_words = re.findall(r'\b\w{4}\b', input_text)
    return four_words

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

print(find_words(text))