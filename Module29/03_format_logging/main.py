from datetime import datetime
from functools import wraps

def log_methods(form_time: str):
    def wrap(cls):
        cur_format = ''.join("%" + elem if elem.isalpha() else elem for elem in form_time)

        list_method = dir(cls)
        for name_method in list_method:
            if not name_method.startswith("__"):
                cur_method = getattr(cls, name_method)

                @wraps(cur_method)
                def wrapper(self, *args, method = cur_method, **kwargs):
                    start_time = datetime.now()

                    print(f"Запускается {cls.__name__}.{cur_method.__name__}. Дата и время запуска: {start_time.strftime(cur_format)}")
                    result = method(self, *args, **kwargs)
                    end_time = datetime.now()
                    print(f"Завершение {cls.__name__}.{cur_method.__name__}, время работы: {(end_time - start_time).total_seconds():.3f} s.")
                    return result

                setattr(cls, name_method, wrapper)

        return cls
    return wrap

@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()