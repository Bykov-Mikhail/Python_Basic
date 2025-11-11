import time
from typing import Callable, Any
import functools

class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Callable:
        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")
        start_time = time.perf_counter()
        res = self.func(*args, **kwargs)
        end_time = time.perf_counter()
        print("Результат:", res)
        print(f"Время выполнения: {end_time - start_time} секунд")
        return self.func

@LoggerDecorator
def complex_algorithm(arg1: int, arg2: int) -> int:
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result

# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)