import random


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")

class Healer(Hero):
    # Целитель:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        self.set_power(self.get_power() * 3)
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    def attack(self, target):
        target.take_damage(self.get_power() / 2)
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage * 1.2))
        super().take_damage(damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    def heal(self, target):
        new_hp = target.get_hp() + self.get_power()
        target.set_hp(new_hp)
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель
    def make_a_move(self, good_team, evil_team):
        move = False
        for hero in good_team:
            if hero.get_hp() < self.max_hp - 30:
                print(f"\n{self.name}: Исцеляю - ", hero.name)
                self.heal(hero)
                return
        else:
            if evil_team:
                print(f"\n{self.name}: Атакую дальнего - ", evil_team[len(evil_team) - 1].name)
                self.attack( evil_team[len(evil_team) - 1])
                return

    def __str__(self):
        return "Имя: {0} | Здоровье: {1}".format(self.name, self.get_hp())

class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    def __init__(self, name):
        super().__init__(name)
        self.indicator_defend = 1
        self.shield = False
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    def attack(self, target):
        target.take_damage(self.get_power() / 2)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage / self.indicator_defend))
        super().take_damage(damage)
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    def up_sheild(self):
        if not self.shield:
            self.shield = True
        self.indicator_defend *= 2
        self.set_power(self.get_power() / 2)
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    def down_sheild(self):
        if self.shield:
            self.shield = False
        self.indicator_defend /= 2
        self.set_power(self.get_power() * 2)
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель
    def make_a_move(self, good_team, evil_team):
        print(f"\n{self.name}: Опускаю щит!")
        self.down_sheild()
        if evil_team:
            print(f"\n{self.name}: Атакую ближнего - ", evil_team[0].name)
            self.attack(evil_team[0])
            print(f"\n{self.name}: Поднимаю щит")
            self.up_sheild()

    def __str__(self):
        return "Имя: {0} | Здоровье: {1}".format(self.name, self.get_hp())

class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    def attack(self, target):
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_down()
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage * (self.power_multiply / 2)))
        super().take_damage(damage)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    def power_up(self):
        self.power_multiply *= 2
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    def power_down(self):
        self.power_multiply /= 2
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
    def make_a_move(self, good_team, evil_team):
        tank_alive = False
        for friend in good_team:
            if isinstance(friend, Tank) and friend.is_alive():
                tank_alive = True

        if tank_alive:
            print(print(f"\n{self.name}: Танк жив, могу подготовить атаку"))
            self.power_up()

        if evil_team:
            print(f"\n{self.name}: Атакую ближнего - {evil_team[0].name}")
            self.attack(evil_team[0])

    def __str__(self):
        return "Имя: {0} | Здоровье: {1}".format(self.name, self.get_hp())

