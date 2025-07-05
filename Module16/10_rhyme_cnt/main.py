list_people = []

quantity_people = int(input("Количество человек: "))

for i in range(1, quantity_people + 1):
    list_people.append(i)

numbers_score = int(input("\nКакое число в считалке? "))

print(f"\nЗначит, выбывает каждый {numbers_score}-й человек")

current_index = 0

while len(list_people) > 1:
    print()
    print(f"\nТекущий круг людей: {list_people}")

    print(f"\nНачало счета с номера {list_people[current_index]}")

    current_index = (current_index + numbers_score - 1) % len(list_people)

    print(f"\nВыбывает человек под номером {list_people.pop(current_index)}")

    if current_index >= len(list_people):
        current_index = 0

print(f"\nОстался человек под номером {list_people[0]}")



