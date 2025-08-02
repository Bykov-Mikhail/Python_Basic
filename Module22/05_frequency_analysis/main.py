eng_alphabet = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
file_text = open('text.txt', 'r')
sum_sym = 0
dict_sym = dict()
for line in file_text:
    for sym in line:
        if sym.lower() in eng_alphabet:
             sum_sym += 1
             if not sym in dict_sym:
                 dict_sym[sym.lower()] = 1
             else:
                 dict_sym[sym.lower()] += 1

for key, value in dict_sym.items():
    dict_sym[key] = (round(value / sum_sym, 3))
temp = sorted(dict_sym.items(), key=lambda x: x[0])
dict_sym = sorted(temp, key=lambda x: x[1], reverse=True)

file_analisys = open('analysis.txt', 'w')

for sym, value in dict_sym:
    file_analisys.write('{key} {value}\n\n'.format(key=sym, value=value))

file_analisys.close()