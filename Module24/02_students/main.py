class Student:
    def __init__(self, sec_name_name, number_group, grade):
        self.sec_name_name = sec_name_name
        self.number_group = number_group
        self.grade = grade

    def info_student(self):
        return "ФИ: {}\nНомер группы: {}\nУспеваемость: {}".format(self.sec_name_name, self.number_group, self.grade)

list_student = []

for index in range(1, 10 + 1):
    while True:
        try:
            sec_name_name = input("\nВведите Фамилию и Имя через пробел: ").split()
            if len(sec_name_name) != 2:
                raise NameError ("\nВведите ФИ через пробел")
            for name in sec_name_name:
                if not name.isalpha():
                    raise NameError ("\nВведите ФИ через пробел(только буквы)")

            number_group = int(input("\nВведите номер группы: "))

            grade = input("\nВведите минимум 5 оценок через пробел: ").split()
            grade = [int(num) for num in grade]
            if len(grade) != 5:
                raise IndexError ("\nНужно ввести 5 оценок через пробел")

            index = Student(sec_name_name, number_group, grade)
            list_student.append(index)
            break
        except IndexError as exc:
            print(exc)
        except NameError as exc:
            print(exc)
        except ValueError as exc:
            print(exc)

sorted_students = sorted(list_student, key=lambda student: (sum(student.grade) / 5), reverse=True)

for student in sorted_students:
    print(student.info_student())
    print()





