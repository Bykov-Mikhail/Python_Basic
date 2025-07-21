goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for item in goods:
    total_quant = 0
    total_price = 0
    flag = True
    for _ in store:
        if flag == False:
                break
        data_inv_nam = store[goods[item]]
        flag = False
        for posit in data_inv_nam:
            total_quant += posit["quantity"]
            total_price += posit["price"] * posit["quantity"]

    print("\n{item} - {quantity} штук, стоимость {price} рубля.".format(item = item, quantity = total_quant, price = total_price))



