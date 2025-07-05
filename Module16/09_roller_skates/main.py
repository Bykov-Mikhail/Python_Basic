list_rental = []
list_people = []

quantity_roll = int(input("Количество роликов: "))

for i in range(quantity_roll):
    size_roll = int(input(f"\nРазмер пары {i + 1}: "))
    list_rental.append(size_roll)

print()
quantity_people = int(input("\nКоличество людей: "))

for i in range(quantity_people):
    size_foot = int(input(f"\nРазмер ноги человека {i + 1}: "))
    list_people.append(size_foot)

count_tenants = 0

for i in list_rental:
    for j in list_people:
        if i == j:
            count_tenants += 1
            break

print(f"\nНаибольшее количество людей, которые могут взять ролики: {count_tenants}")

