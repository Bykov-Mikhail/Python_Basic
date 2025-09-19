import random

class KillError(Exception):
    """
    Класс: KillError Родитель: Exception
    """
    def __str__(self):
        """
        Метод для переопределения вывода ошибки: KillError

        :return: "Ошибка: Убийство"
        :rtype: str
        """
        return "Ошибка: Убийство"
class DrunkError(Exception):
    """
    Класс DrunkError Родитель: Exception
    """
    def __str__(self):
        """
        Метод для переопределения вывода ошибки: DrunkError
        :return: "Ошибка: Пьянство"
        :rtype: str
        """
        return "Ошибка: Пьянство"
class CarCrashError(Exception):
    """
    Класс: CarCrashError Родитель: Exception
    """
    def __str__(self):
        """
        Метод для переопределения вывода ошибки: CarCrashError
        :return: "Ошибка: Разбиение машины"
        :rtype: str
        """
        return "Ошибка: Разбиение машины"
class GluttonyError(Exception):
    """
    Класс: GluttonyError Родитель: Exception
    """
    def __str__(self):
        """
        Метод для переопределения вывода ошибки: GluttonyError
        :return: "Ошибка: Обжорство"
        :rtype: str
        """
        return "Ошибка: Обжорство"
class DepressionError(Exception):
    """
    Класс: DepressionError Родитель: Exception
    """
    def __str__(self):
        """
        Метод для переопределения вывода ошибки: DepressionError
        :return: "Ошибка: Депрессия"
        :rtype: str
        """
        return "Ошибка: Депрессия"

def one_day():
    probability = random.randint(1, 10)
    if probability == 1:
        raise random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
    else:
        karma = random.randint(1, 7)
        return karma

count_day = 1
count_karma = 0
with open('karma.log', 'a', encoding = 'utf-8') as file:
    while count_karma < 500:
        try:
            count_karma += one_day()
            print("День {}:".format(count_day))
            print(" Карма - {}\n".format(count_karma))
            count_day += 1

        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            count_day += 1
            file.write('\nДень {}:\n  {}'.format(count_day - 1, exc))


