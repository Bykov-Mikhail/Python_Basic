import random

numbers = [random.randint(0, 100) for _ in range(10)]
print("Оригинальный список:", numbers)

first_decision = [(numbers[i], numbers[i + 1]) for i in range(len(numbers)) if i % 2 == 0]
print("\nПервое решение:", first_decision)

second_decision = [(numbers[i - 1], numbers[i]) for i in range(len(numbers)) if i % 2 != 0]
print("\nВторое решение:",second_decision)
