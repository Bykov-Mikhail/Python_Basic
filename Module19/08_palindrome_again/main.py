def check_palindrom(text):
    sym_quant = dict()
    for sym in text:
        if sym in sym_quant:
            sym_quant[sym] += 1
        else:
            sym_quant[sym] = 1
    count_odd = 0
    for sym in sym_quant:
        if sym_quant[sym] % 2 != 0:
            count_odd += 1
    if len(text) % 2 == 0 and count_odd == 0:
        return True
    elif len(text) % 2 != 0 and count_odd == 1:
        return True
    else:
        return False

input_text = input("Введите строку: ")

if check_palindrom(input_text):
    print("\nМожно сделать палиндромом")
else:
    print("\nНельзя сделать палиндромом")