violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

quantity_songs = int(input("Сколько песен выбрать? "))
total_time = 0
for num in range(quantity_songs):
    name_song = input("\nНазвание {0} песни: ".format(num + 1))
    if name_song in violator_songs.keys():
        total_time += violator_songs[name_song]
    else:
        print("\nТакой песни нет в нашем списке.")

print("\nОбщее время звучания песен: {:.2f} минуты".format(total_time))


