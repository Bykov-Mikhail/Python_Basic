from typing import Callable

def decorator_with_args_for_any_decorator(original_decorator):
    def wrap(*decor_args, **decor_kwargs):
        def actual_decorator(func):
            return original_decorator(func, *decor_args, **decor_kwargs)
        return actual_decorator
    return wrap

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    def wrap(*func_args, **func_kwargs):
        print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
        return func(*func_args, **func_kwargs)
    return wrap


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)