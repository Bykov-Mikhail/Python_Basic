import random
def chance_1_in_13():
    return random.random() < 1/13

def hell_cycle():
    sum_number = 0

    while sum_number <= 777:
        try:
            number = int(input("\nВведите число: "))
        except ValueError as exc:
            print("\nОшибка: Введите число")
            continue

        sum_number += number
        if chance_1_in_13():
            print("\nВас постигла неудача!")
            break
        with open('out_file.txt', 'a') as file:
            file.write(str(number) + '\n' * 2)
    else:
        print("\nВы успешно выполнили условие для выхода из порочного цикла!")


hell_cycle()
