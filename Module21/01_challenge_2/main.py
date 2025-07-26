def all_numbers(num):
    if num == 0:
        return 0
    all_numbers(num - 1)
    print("\n", num)

number = int(input("Введите num: "))
all_numbers(number)
