alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч','ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

input_text = input("Введите сообщение: ")
shift = int(input("\nВведите сдвиг: "))
code_word = []

for sym in input_text:
    if sym in alphabet:
        index = alphabet.index(sym)
        new_index = (index + shift) % len(alphabet)
        code_word.append(alphabet[new_index])
    else:
        code_word.append(sym)

print()
print("".join(code_word))