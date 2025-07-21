def no_set_sim(num_1, num_2, num_3):
    list_similar_num = []
    for i in num_3:
        if i in num_2:
            if i in num_1:
                list_similar_num.append(i)
    return list_similar_num

def set_sim(num_1, num_2, num_3):
    res_set = set(num_1) & set(num_2) & set(num_3)
    return res_set

def no_set_diff(num_1, num_2, num_3):
    list_diff = []
    for i in num_1:
        if i not in num_2:
            if i not in num_3:
                list_diff.append(i)
    return list_diff

def set_diff(num_1, num_2, num_3):
    res_set = (set(array_1) - set(array_2)) - set(array_3)
    return res_set

array_1 = [1, 5, 10, 20, 40, 80, 100]

array_2 = [6, 7, 20, 80, 100]

array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print("Задача 1:")
print("Решение без множеств:", *no_set_sim(array_1, array_2, array_3))
print("Решение с множествами:", *set_sim(array_1, array_2, array_3))

print("\nЗадача 2:")
print("Решение без множеств:", *no_set_diff(array_1, array_2, array_3))
print("Решение с множествами:", *set_diff(array_1, array_2, array_3))