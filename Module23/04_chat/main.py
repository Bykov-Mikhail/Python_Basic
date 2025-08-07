import os

def chat(name):
    if not os.path.exists("My_app_Chat"):
         os.mkdir("My_app_Chat")
    path_chat = os.path.join('My_app_Chat', 'chat.txt')
    path_chat_log = os.path.join('My_app_Chat', 'log.txt')
    while True:
        with open(path_chat_log, 'a', encoding='utf-8') as file_log:
            try:
                choose_action = input("Выберите одно из действий:\n\n"
                                      "   1.Посмотреть текущий текст чата.\n"
                                      "   2.Отправить сообщение.\n"
                                      "   Введите 1 или 2: ")
                if int(choose_action) == 1:
                    with open(path_chat, 'a', encoding='utf-8') as file_chat:
                        file_chat.close()
                    with open(path_chat, 'r', encoding='utf-8') as file_chat:
                        print((file_chat.read()))
                elif int(choose_action) == 2:
                    message = input("\nВведите сообщение: ")
                    with open(path_chat, 'a', encoding='utf-8') as file_chat:
                        file_chat.write('\n{name}:\n'.format(name=str(name)) + '   {message}'.format(message=str(message)) + '\n')
                else:
                    raise ValueError
            except ValueError:
                print("\nОшибка: Нужно ввести 1 или 2\n")
                file_log.write("Пользователь {name} ввел {choose_action} вместо 1 или 2".format(name=str(name), choose_action=str(choose_action) + '\n' * 2))
                continue
            except FileNotFoundError:
                print("\nОшибка: Проблема с созданием пути чата(попробуйте перезапустить программу)\n")
                file_log.write("Путь создания чата: {path_chat}".format(path_chat=path_chat))

name_user = input("Введите имя пользователя: ")

chat(name_user)