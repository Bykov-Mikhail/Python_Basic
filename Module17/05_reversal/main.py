input_string = input("Введите строку: ")

start = input_string.rindex("h")
stop = input_string.find("h")

print(f"\nРазвернутая последовательность между первым и последним h: {input_string[start - 1:stop:-1]}")




