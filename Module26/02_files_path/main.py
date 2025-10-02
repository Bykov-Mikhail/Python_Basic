from collections.abc import Iterable
import os

def gen_files_path(root : str , disk_find: str | None = None) -> Iterable[str]:
    flag_find = False
    try:
        for root, dirs, files in os.walk(os.path.join(disk_find.upper() + ':', os.sep, root) if disk_find else os.sep + root):
            for file in files:
                yield os.path.join(root, file)
            flag_find = True

        if not flag_find:
            raise FileNotFoundError

    except FileNotFoundError:
        if disk_find:
            print("\nОшибка: На указанном диске нет заданной директории")
            print(os.path.join(disk_find.upper() + ':', root))
        else:
            print("\nВ корне диска нет указанной директории")


name_dir = input("Введите название директории: ")

for path in gen_files_path(name_dir):
    print(path)

