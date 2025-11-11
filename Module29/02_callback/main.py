from typing import Callable
class App:
    """Класс представляет веб приложение с маршрутизацией"""
    def __init__(self):
        """Инициализирует пустой словарь маршрутов"""
        self.routes = {}

    def get(self, path: str) -> Callable:
        """
        Возвращает функцию указанного пути
        :param path: Путь (URL - маршрут)
        :return: Функция обработчик или None, если путь не найден.
        """
        return self.routes.get(path)

app = App()

def callback(path: str) -> Callable:
    """
    Декоратор, который привязывает путь к функции
    :param path: строка(путь)
    """
    def decor(func: Callable) -> Callable:
        """
        Декорируем функцию
        :param func: декорируемая функция
        :return: декорированная функция
        """
        app.routes[path] = func
        return func
    return decor

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')