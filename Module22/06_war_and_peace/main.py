import zipfile

with zipfile.ZipFile('voina-i-mir.zip', 'r') as zipf:
    with zipf.open('voyna-i-mir.txt') as file:
        text = file.read()
        decod_text = text.decode('utf-8')

        dict_sym = dict()
        rus_alphabet_sm = [chr(letter) for letter in range(ord('а'), ord('я') + 1)]
        eng_alphabet_sm = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
        rus_alphabet_bg = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]
        eng_alphabet_bg = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]
        total_alphabet = rus_alphabet_sm + eng_alphabet_sm + rus_alphabet_bg + eng_alphabet_bg

        for line in decod_text:
            for sym in line:
                if sym in total_alphabet:
                    dict_sym[sym] = dict_sym.get(sym, 0) + 1

        dict_sym = sorted(dict_sym.items(), key= lambda x: x[1], reverse=True)

with open('result.txt', 'w', encoding='utf-8') as res_file:
    for key, value in dict_sym:
        res_file.write('{key}: {value}'.format(key=key, value=value) + '\n' * 2)


