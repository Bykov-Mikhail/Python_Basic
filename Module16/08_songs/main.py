violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

quantity_songs = int(input("Сколько песен выбрать? "))
total_time = 0

for number_songs in range(quantity_songs):
    input_song = input(f"\nНазвание {number_songs + 1}-й песни: ")
    for song in violator_songs:
        if input_song == song[0]:
            total_time += song[1]

print(f"\nОбщее время звучания - {round(total_time, 2)} минуты")