import requests
import re

input_link = input("Введите ссылку сайта: ")
req = requests.get(str(input_link))

def all_h3(request: str) -> list[str]:
    """
    Функция обрабатывает html страницы и находит все заголовки h3

    :param request: htm формат страницы
    :return: Список заголовков h3
    """
    list_h3 = re.findall(r'<h3>(.*?)</h3>', request)
    return list_h3

print(all_h3(req.text))

