class Matrix:
    def __init__(self, data,  quantity_row=None, quantity_col=None):
        self.quantity_row = quantity_row
        self.quantity_col = quantity_col
        self.data = data

    def __str__(self):
        lines = []
        for row in self.data:
            line = str(row)
            lines.append(line)
        return '\n'.join(lines)

    def __add__(self, other_matrix):
        if self.quantity_row == other_matrix.quantity_row and self.quantity_col == other_matrix.quantity_col:

            new_data = []
            for row in range(self.quantity_row):
                new_row = [x + y for x, y in zip(self.data[row], other_matrix.data[row])]
                new_data.append(new_row)

            return Matrix(new_data)

        else:
            raise ValueError("Ошибка: Матрицы должны быть одинакового размера")

    def __sub__(self, other_matrix):
        if self.quantity_row == other_matrix.quantity_row and self.quantity_col == other_matrix.quantity_col:

            new_data = []
            for row in range(self.quantity_row):
                new_row = [x - y for x, y in zip(self.data[row], other_matrix.data[row])]
                new_data.append(new_row)

            return Matrix(new_data)
        else:
            raise ValueError("Ошибка: Матрицы должны быть одинакового размера")
    def __mul__(self, other_matrix):
        if self.quantity_col == other_matrix.quantity_row:

            new_data = []
            for row in range(self.quantity_row):
                new_row = []
                for col_other in range(other_matrix.quantity_col):
                    summ = 0
                    for col in range(self.quantity_col):
                        summ += self.data[row][col] * other_matrix.data[col][col_other]

                    new_row.append(summ)

                new_data.append(new_row)

            return Matrix(new_data)

        else:
            raise ValueError("Ошибка: Количество колонн в умножаемом не равно количеству строк в множителе.")

    def transpose(self):
        new_data = []
        for i in range(self.quantity_col):
            new_row = []
            for j in range(self.quantity_row):
                new_row.append(self.data[j][i])
            new_data.append(new_row)
        return Matrix(new_data)

# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix([[1, 2, 3], [4, 5, 6]], 2, 3)

m2 = Matrix([[7, 8, 9], [10, 11, 12]], 2, 3)

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1 + m2)

print("Вычитание матриц:")
print(m1 - m2)

m3 = Matrix([[1, 2], [3, 4], [5, 6]], 3, 2)

print("Умножение матриц:")
print(m1 * m3)

print("Транспонирование матрицы 1:")
print(m1.transpose())