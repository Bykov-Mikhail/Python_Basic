word = input("Введите слово: ")

word_reverse = ''

for i in word:
    word_reverse = i + word_reverse

if word == word_reverse:
    print("\nСлово является палиндромом.")
else:
    print("\nСлово не является палиндромом.")