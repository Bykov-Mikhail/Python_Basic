list_numbers = []
count_numbers = 0

quantity_numbers = int(input("Количество чисел: "))

for i in range(quantity_numbers):
    input_number = int(input("\nЧисло: "))
    list_numbers.append(input_number)

def check_palindrome(list):
    for i in range (len(list) // 2):
        if list[i] != list[len(list) - 1 - i]:
            return False
    return True

if check_palindrome(list_numbers):
    print(f"\nПоследовательность: {list_numbers}")
    print("\nНичего добавлять не нужно.")
else:
    add_list = []

    for i in range(len(list_numbers)):
        temp_list = list_numbers.copy()
        for j in range(i - 1, -1, -1):
            temp_list.append(list_numbers[j])

        if check_palindrome(temp_list):
            for j in range(i - 1, -1, -1):
                add_list.append(list_numbers[j])
            break


    print(f"\nПоследовательность: {list_numbers}")
    print(f"\nНужно приписать чисел: {len(add_list)}")
    print(f"\nСами числа: {add_list}")




