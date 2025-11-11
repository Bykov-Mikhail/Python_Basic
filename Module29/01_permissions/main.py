from functools import wraps
from typing import Any, Callable, List

def check_permission(required_permission: List[str]) -> Callable:
    """
    Декоратор, который проверяет права для выполнения функции
    :param required_permission: требуемые права
    :return: Декорированная функция
    """
    def decor(func: Callable) -> Callable:
        @wraps(func)
        def wrap(*args : Any, **kwargs : Any) -> Any:
            if not any(perm in user_permissions for perm in required_permission):
                raise PermissionError(f"у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")
            return func(*args, **kwargs)
        return wrap
    return decor

user_permissions = ['admin']

@check_permission(['admin', 'moderator'])
def delete_site():
    print('Удаляем сайт')

@check_permission(['user_1', 'moderator'])
def add_comment():
    print('Добавляем комментарий')

delete_site()
add_comment()