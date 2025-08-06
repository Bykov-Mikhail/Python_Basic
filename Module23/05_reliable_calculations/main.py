import math

def get_sage_sqrt(num):
    try:
        if (type(num) == int or type(num) == float) and num >= 0:
            res = math.sqrt(num)
            return res
        else:
            raise ValueError
    except ValueError as exc:
        print("\nОшибка типа данных {num}".format(num=num), type(exc))

# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"\nКвадратный корень numbers {number}: {result}")