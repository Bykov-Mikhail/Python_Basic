def quantity_sym(name_file):
    list_name = []
    errors = []
    sum_sym = 0

    try:
        with open(name_file, 'r', encoding='utf-8') as people:
            for line in people:
                if line != '\n':
                    list_name.append(line.strip())

        for index, name in enumerate(list_name):
            if len(name) < 3:
                print("Ошибка: менее трех символов в строке {}\n".format(index + 1))
                errors.append("Ошибка: менее трех символов в строке {}".format(index + 1))
            sum_sym += len(name)

        if errors:
            with open('errors.log', 'a', encoding='utf-8') as file_errors:
                for err in errors:
                    file_errors.write(err + '\n' * 2)

        return print("\nОбщее количество символов:", sum_sym)
    except FileNotFoundError as exc:
        print(exc)

quantity_sym('people.txt')

