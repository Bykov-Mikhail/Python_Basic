import random

class Parent:
    def __init__(self, name, age, list_children):
        self.name = name
        self.age = age
        self.list_children = []

        for child in list_children:
            if age - child.age < 16:
                print(f"Ошибка: {child.name} слишком стар для родителя {name}")
            else:
                self.list_children.append(child)

    def info_parent(self):
        print(f"\nИмя: {self.name}\n\nВозраст: {self.age}\n\nДети: {', '.join(child.name for child in self.list_children)}\n\n")

    def calm(self, child):
        print(f"{self.name} успокаивает {child.name}")
        child.state_clam = True

    def feed(self, child):
        print(f"{self.name} Кормит {child.name}")
        child.state_eat = False

class Children:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.state_calm = random.choice([False, True])
        self.state_eat = random.choice([False, True])

    def skip_time(self):
        self.state_calm = random.choice([False, True])
        self.state_eat = random.choice([False, True])


child_1 = Children("Костя", 4)

child_2 = Children("Маша", 5)

parent_1 = Parent("Артем", 25, [child_1, child_2])

hours = 0
parent_1.info_parent()
while hours < 3:
    if child_1.state_calm == False:
        parent_1.calm(child_1)
    if child_1.state_eat == True:
        parent_1.feed(child_1)
    if child_2.state_calm == False:
        parent_1.calm(child_2)
    if child_2.state_eat == True:
        parent_1.feed(child_2)

    child_1.skip_time()
    child_2.skip_time()
    hours += 1
    print()
