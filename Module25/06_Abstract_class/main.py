import math

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        square = math.pi * self.radius ** 2
        return round(square, 2)

class Rectangle(Shape):
    def __init__(self, first_side, second_side):
        super().__init__()
        self.first_side = first_side
        self.second_side = second_side

    def area(self):
        square = self.first_side * self.second_side
        return round(square, 2)

class Triangle(Shape):
    def __init__(self, side, height):
        super().__init__()
        self.side = side
        self.height = height

    def area(self):
        square = (self.side * self.height) / 2
        return square

# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
