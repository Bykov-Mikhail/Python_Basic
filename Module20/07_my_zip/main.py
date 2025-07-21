def my_zip(data_1, data_2):
    if isinstance(data_1, dict):
        data_1 = data_1.keys()
    elif isinstance(data_2, dict):
        data_2 = data_2.keys()
    if len(data_1) <= len(data_2):
        return ((elem, data_2[index]) for index, elem in enumerate(data_1))
    elif len(data_2) < len(data_1):
        return ((data_1[index], elem) for index, elem in enumerate(data_2))

text = "abcd"

tuple_num = (10, 20, 30, 40,)

result = my_zip(text, tuple_num)

print(my_zip(text, tuple_num))
for i in result:
    print("\n",i)


