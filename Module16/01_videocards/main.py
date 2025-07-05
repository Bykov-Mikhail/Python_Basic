quantity_videocard = int(input("Количество видеокарт: "))

videocard_list = []
max_number = 0

for number_card in range(quantity_videocard):
    videocard = int(input(f"\nВидеокарта {number_card + 1}: "))
    videocard_list.append(videocard)

print()
print(f"\nСтарый список видеокарт: {videocard_list}")

for card in videocard_list:
    if card > max_number:
        max_number = card

for _ in videocard_list:
    if max_number in videocard_list:
        videocard_list.remove(max_number)

print(f"\nНовый список видеокарт: {videocard_list}")


