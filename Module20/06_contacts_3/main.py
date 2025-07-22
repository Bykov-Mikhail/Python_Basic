def add_contact(base):
    name, surname = input("\nВведите имя и фамилию нового контакта (через пробел): ").title().split()
    name_contact = (name, surname)

    if name_contact in base:
        print("\nТакой человек уже есть в контактах.")
        return base

    number_phone = input("\nВведите номер телефона: ")
    base[name_contact] = number_phone

    return base

def find_contact_book(base):
    surname = input("\nВведите фамилию для поиска: ").title()
    for key, value in base.items():
        if key[1] == surname:
            return *key, value
    else:
        return False

data_base_contact = dict()
while True:
    print("Введите номер действия:")

    action = int(input("\n     1.Добавить контакт."
                       "\n     2.Найти человека."
                       "\n     3.Закрыть телефонную книгу"
                       "\n     № действия: "))
    if action == 1:
        print("\nТекущий словарь контактов:", add_contact(data_base_contact))
        print()
        continue
    elif action == 2:
        find_contact = find_contact_book(data_base_contact)
        if  not find_contact:
            print("\nКонтакта с такой фамилией нет в телефонной книге")
            print()
            continue
        else:
            print("\n", *find_contact)
            print()
    elif action == 3:
        break
    else:
        print("\nОшибка ввода.")
        print()
        continue
