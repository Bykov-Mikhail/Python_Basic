def merge_sorted_lists(list1, list2):

    list1.extend(list2)

    for i in range(len(list1) - 1):
        number = list1[i]
        for _ in list1:
            if list1.count(number) > 1:
                list1.remove(number)

    for i in range(len(list1)):
        max_number = 0
        for j in range(1, len(list1) - i):
            if list1[j] > list1[max_number]:
                max_number = j
        list1[max_number], list1[len(list1) - 1 - i] = list1[len(list1) - 1 - i], list1[max_number]

    return list1



# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

merged = merge_sorted_lists(list1, list2)
print(merged)