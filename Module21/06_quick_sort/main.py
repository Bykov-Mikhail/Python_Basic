def recurs_sup_list(sup_list):
    if not sup_list:
        return []
    result = []
    result.extend(support_sort(sup_list))
    return result

def support_sort(list_num):
    sup_elem = list_num[-1]
    less_sup = []
    equally_sup = []
    more_sup = []
    for elem in list_num:
        if elem < sup_elem:
            less_sup.append(elem)
        elif elem == sup_elem:
            equally_sup.append(elem)
        elif elem > sup_elem:
            more_sup.append(elem)
    return quick_sort(less_sup, equally_sup, more_sup)

def quick_sort(less, equal, more):
    recurs_sup_list(less)
    recurs_sup_list(more)

    return recurs_sup_list(less) + equal + recurs_sup_list(more)

numbers = [5, 8, 9, 4, 2, 9, 1, 8]

print(support_sort(numbers))
