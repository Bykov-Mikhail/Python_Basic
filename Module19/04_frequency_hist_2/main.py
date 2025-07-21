def origin_dict(dict):
    for key, value in sorted(dict.items()):
        print("\n", key, ":", value)

def invert_dict(dict):
    min_num = 1
    while min_num - 1 < max(dict.values()):
        list_sym = [elem for elem in dict if dict[elem] == min_num]
        print("\n", min_num, ":", list_sym)
        min_num += 1

sym_dict = dict()
input_text = input("Введите текст: ")

for sym in input_text:
    sym_dict[sym] = sym_dict.get(sym, 0) + 1

print("\nОригинальный словарь частот:")
origin_dict(sym_dict)

print("\nИнвертированный словарь частот:")
invert_dict(sym_dict)




