quantity_orders = int(input("Введите количество заказов: "))
data_orders = dict()


for num in range(1, quantity_orders + 1):
    orders = dict()
    order = input("\n{0} заказ: ".format(num)).split()
    name = order[0]
    pizza = order[1]
    quantity = int(order[2])
    if name not in data_orders:
        data_orders[name] = {}
    if pizza in data_orders[name]:
            data_orders[name][pizza] += quantity
    else:
        data_orders[name][pizza] = quantity

for name in data_orders.keys():
    print("\n{0}:".format(name))
    for ord in sorted(data_orders[name]):
        print("\n", ord, ":", data_orders[name][ord])


