class Property:
    """
    Базовый класс, описывающий собственность

    Args:
        worth (int): передается стоимость имущества
    """
    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        """
        Геттер для получения стоимости имущества
        :return: __worth
        :rtype: int
        """
        return self.__worth

    def calc_tax(self):
        pass

class Apartment(Property):
    """
    Класс Apartment. Родитель: Property

    Args:
        worth (int): передается стоимость имущества
    """
    def calc_tax(self):
        """
        Метод для подсчета налога на Apartment

        :return: tax
        :rtype: int
        """
        tax = self.get_worth() / 1000
        return tax

class Car(Property):
    """
    Класс Car. Родитель: Property

    Args:
        worth (int): передается стоимость имущества
    """
    def calc_tax(self):
        """
        Метод для подсчета налога на Car

        :return: tax
        :rtype: int
        """
        tax = self.get_worth() / 200
        return tax

class CountryHouse(Property):
    """
    Класс CountryHouse. Родитель: Property

    Args:
        worth (int): передается стоимость имущества
    """
    def calc_tax(self):
        """
        Метод для подсчета налога на CountryHouse

        :return: tax
        :rtype: int
        """
        tax = self.get_worth() / 500
        return tax
while True:
    try:
        choice_type_tax = int(input("Выберите тип налога.\n1 - Квартира\n2 - Машина\n3 - Дача\nВведите цифру: "))
        if choice_type_tax < 1 or choice_type_tax > 3:
            raise ValueError("Ошибка: Для выбора типа налога введите 1/2/3")
        quantity_money = int(input("\nВведите количество денег: "))
        if quantity_money <= 0:
            raise ValueError("Ошибка: Количество денег не может быть меньше или равно 0")
        property_value = int(input("\nВведите стоимость имущества: "))
        if property_value <= 0:
            raise ValueError("Ошибка: Стоимость имущества не может быть меньше или равно 0")
        break
    except ValueError as exc:
        print(exc)

if choice_type_tax == 1:
    tax = Apartment(property_value).calc_tax()
elif choice_type_tax == 2:
    tax = Car(property_value).calc_tax()
elif choice_type_tax == 3:
    tax = CountryHouse(property_value).calc_tax()

print("\nСтоимость налога: {tax}".format(tax=tax))

if tax > quantity_money:
    lack = tax - quantity_money
    print("\nДля оплаты налога вам не хватает: {}".format(lack))
else:
    print("\nВы оплатили налог!")
    quantity_money -= tax
    if quantity_money:
        print("\nОстаток средств: {}".format(quantity_money))

