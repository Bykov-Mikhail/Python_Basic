import math
def crypto(data):
    result = []
    if isinstance(data, dict):
        data = data.values()
    for index, elem in enumerate(data):
        if check_past_num(index):
            result.append(elem)
    return result

def check_past_num(index_element):
    if index_element < 2:
        return False
    if index_element == 2:
        return True
    if index_element % 2 == 0:
        return False
    for num in range(3, int(math.sqrt(index_element)) + 1, 2):
        if index_element % num == 0:
            return False
    return True

print(crypto('О Дивный Новый мир!'))