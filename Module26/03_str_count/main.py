import os
from collections.abc import Iterable

def quantity_str(disk: str, name_dir: str) -> Iterable[int]:
    file_find = False
    try:
        for root, dirs, files in os.walk(os.path.join(disk.upper() + ':', os.sep, name_dir)):
            for file in files:
                flag_comm = False
                counter_str = 0
                if file.endswith('.py'):
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as py_file:
                       for line in py_file:
                            if not line.strip():
                                continue

                            if line.startswith('#'):
                                continue

                            if ((line.strip().startswith('"""') and line.strip().endswith('"""') and len(line.strip()) > 5) or
                                    (line.strip().startswith("'''") and line.strip().endswith("'''") and len(line.strip()) > 5)):
                                continue

                            if line.strip() in ('"""', "'''") and not flag_comm :
                                flag_comm = True
                                continue

                            if flag_comm and line.strip() in ('"""', "'''"):
                                flag_comm = False
                                continue

                            if flag_comm:
                                continue

                            counter_str += 1

                       yield counter_str

            file_find = True

        if not file_find:
            raise FileNotFoundError

    except FileNotFoundError:
        print("\nОшибка: путь: {path} не найден".format(path = os.path.join(disk.upper() + ':', os.sep, name_dir)))

input_disk = input("Введите букву диска: ")
input_name_dir = input("Введите имя директории: ")
print()

for num, count in enumerate(quantity_str(input_disk, input_name_dir), start=1):
    print(f"Файл №{num} = {count} строк", end = '\n')
