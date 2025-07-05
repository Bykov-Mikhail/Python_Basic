numbers_list = [1, 4, -3, 0, -10]
new_list = []
len_list = len(numbers_list)

shift = int(input("Сдвиг: "))

print(f"Изначальный список: {numbers_list}")

for i in range(len_list - 1, -1 , -1):
    new_list.append(numbers_list[(len_list - 1) - (shift + i)])



print(f"Сдвинутый список: {new_list}")


