import os

def find_file(path):
    quantity_files = 0
    sum_weight = 0
    quantity_sub_dir = 0

    for item in os.listdir(path):
        check_path = os.path.join(path, item)
        if not os.path.isdir(check_path):
            sum_weight += os.path.getsize(check_path)
            quantity_files += 1
        elif os.path.isdir(check_path):
            quantity_sub_dir += 1
            res = find_file(check_path)
            if res:
                sum_weight += res[0]
                quantity_files += res[1]
                quantity_sub_dir += res[2]

    return sum_weight, quantity_files, quantity_sub_dir

input_path = input("Введите путь: ")

sum_weight, quantity_files, quantity_sub_dir = find_file(input_path)

print("\nРазмер каталога (в Килобайтах):", sum_weight / 1024)
print("\nКоличество подкаталогов:", quantity_sub_dir)
print("\nКоличество файлов:", quantity_files)

