import random

class Warrior:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.is_alive = True

    def attack(self, enemy):
        if self.is_alive and enemy.is_alive:
            print("{} атакует!".format(self.name))
            enemy.take_damage(20)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            print("{} повержен!".format(self.name))
        else:
            print("У {} осталось {} здоровья\n".format(self.name, self.health))

warrior_1 = Warrior("Воин 1")
warrior_2 = Warrior("Воин 2")
warriors = [warrior_1, warrior_2]

print(f"{warrior_1.name}: {warrior_1.health} здоровья\n{warrior_2.name}: {warrior_2.health} здоровья\n")

while warrior_1.is_alive and warrior_2.is_alive:
    attacker = random.choice(warriors)
    if attacker == warrior_1:
        enemy = warrior_2
    else:
        enemy = warrior_1

    attacker.attack(enemy)

if warrior_1.is_alive:
    print("\n{} одержал победу".format(warrior_1.name))
else:
    print("\n{} одержал победу".format(warrior_2.name))


