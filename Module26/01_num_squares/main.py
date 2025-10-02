from collections.abc import Iterator, Iterable

#Класс-итератор
"""
class Square:
    def __init__(self, stop_n: int) -> None :
        self.stop_n = stop_n
        self.counter = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.counter != self.stop_n:
            self.counter += 1
            res = self.counter ** 2
            return res
        else:
            raise StopIteration()

number = Square(5)
for index, num in enumerate(number, start=1):
    print("{index} ** 2 = {num}".format(index=index, num=num))
"""

#Функция-генератор
"""
def square(stop_number: int) -> Iterable[int]:
    counter = 0
    while counter != stop_number:
        counter += 1
        yield counter ** 2

for index, num in enumerate(square(5), start=1):
    print("{index} ** 2 = {num}".format(index=index, num=num))
"""

#Генераторное выражение
stop_number = 5
square = (num ** 2 for num in range(1, stop_number + 1))

for index, num in enumerate(square, start=1):
    print("{index} ** 2 = {num}".format(index=index, num=num))

