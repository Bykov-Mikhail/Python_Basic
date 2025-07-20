quantity = int(input("Введите количество пар слов: "))
synonyms = dict()

for i in range(1, quantity + 1):
    pair = input("\n{0} пара: ".format(i)).title().split(" - ")
    synonyms[pair[0]] = pair[1]
    synonyms[pair[1]] = pair[0]

while True:
    word = input("\nВведите слово: ").capitalize()
    if word in synonyms:
        print("\nСиноним:", synonyms[word])
        break
    else:
        print("\nТакого слова в словаре нет.")



