len_list = int(input("Введите длину списка: "))

list_gen = [(1 if num % 2 == 0 else num % 5) for num in range(len_list)]

print(f"\nРезультат: {list_gen}")
