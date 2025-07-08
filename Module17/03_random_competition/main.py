import random

first_team = [round(random.uniform(5.00, 10.00 ), 2) for _ in range(20)]
second_team = [round(random.uniform(5.00, 10.00 ), 2) for _ in range(20)]
win_team = [(first_team[i] if first_team[i] > second_team[i] else second_team[i]) for i in range(20)]

print(f"Первая команда: {first_team}")
print(f"\nВторая команда: {second_team}")
print(f"\nПобедители тура: {win_team}")

