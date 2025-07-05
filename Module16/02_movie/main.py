films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

top_user = []
quantity_films = int(input("Сколько фильмов хотите добавить? "))
count_add_film = 0

while count_add_film < quantity_films:
    film = input("\nВведите название фильма: ")
    if film in films:
        count_add_film += 1
        top_user.append(film)
    else:
        print(f"\nОшибка: фильма {film} у нас нет :(")


print(f"\nВаш список любимых фильмов: {top_user}")

