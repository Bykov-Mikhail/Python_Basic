import random

class House:
    refrigerator_food = 50
    nightstand_money = 0

class Human:
    my_home = House()

    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def eat(self):
        print("\nАм-Ам-Ам ({})".format(self.name))
        self.satiety += 50
        self.my_home.refrigerator_food -= 5


    def work(self):
        print("\nПоработаем! ({})".format(self.name))
        self.my_home.nightstand_money += 100
        self.satiety -= 40


    def game(self):
        print("\nЖизнь-игра ({})".format(self.name))
        self.satiety -= 30


    def walk_magazine(self):
        print("\nПополняем запасы еды ({})".format(self.name))
        self.my_home.refrigerator_food += 5
        self.my_home.nightstand_money -= 100


    def skip_day(self):
        dice = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.my_home.refrigerator_food < 10:
            self.walk_magazine()
        elif self.my_home.nightstand_money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.game()

    def info_house(self):
        print("\nДеньги: {}\nКол-во еды: {}".format(self.my_home.nightstand_money, self.my_home.refrigerator_food))

human_1 = Human('Миша')
human_2 = Human("Катя")
counter_day = 0
while counter_day < 365:
    print("\nДень начался!")
    human_1.skip_day()
    human_2.skip_day()
    counter_day += 1
    human_1.info_house()
    print("Прожито дней: {}\n\n".format(counter_day))