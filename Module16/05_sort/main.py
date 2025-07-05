list_numbers = [1, 4, -3, 0, 10]
len_list = len(list_numbers)

for i in range(len_list):
    max_number = list_numbers[0]
    max_index = 0
    for j in range(1, len_list - i):
        if max_number < list_numbers[j]:
            max_number = list_numbers[j]
            max_index = j
    list_numbers[max_index], list_numbers[(len_list - 1) - i] = list_numbers[(len_list - 1) - i], list_numbers[max_index]

print(list_numbers)