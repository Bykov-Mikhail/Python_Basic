text = input("Введите текст: ")

list_vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

list_sym = [sym for sym in text if sym in list_vowels]

print(f"Список гласных букв: {list_sym}")

print(f"\nДлина списка: {len(list_sym)}")



