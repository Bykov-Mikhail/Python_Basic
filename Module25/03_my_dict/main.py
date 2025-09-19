class MyDict(dict):
    """
    Класс: MyDict Родитель: dict
    Переопределяет метод get: если ключ не найден, возвращает 0
    """
    def get(self, key, default = 0):
        """
        Метод возвращает значение по ключу. Если ключа нет - возвращает default
        :param key: Ключ для поиска в словаре
        :param default: Значение по умолчанию, если ключ не найден
        :return: значение по ключу или default
        """
        return super().get(key, default)

my_dict = MyDict({'a': 1, 'b': 2, 'c': 3})
print(my_dict.get('d'))
