nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def open_list(list_of_lists):
    if not isinstance(list_of_lists, list):
        return [list_of_lists]
    result = []
    for elem in list_of_lists:
        result.extend(open_list(elem))
    return result

print(open_list(nice_list))