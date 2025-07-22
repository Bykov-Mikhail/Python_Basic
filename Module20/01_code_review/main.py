def function_find(data_students):
    list_interests = list()
    string = ''
    for index in data_students:
        list_interests += (data_students[index]['interests'])
        string += data_students[index]['surname']
    len_surnames = len(string)
    return set(list_interests), len_surnames

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

pairs = [(i, students[i]["age"]) for i in students]

my_list_interests, total_len_surname  = function_find(students)

print("Результат работы программы:")
print("\nСписок пар «ID студента — возраст»:", pairs)
print("\nПолный список интересов всех студентов:", my_list_interests)
print("\nОбщая длина всех фамилий студентов:", total_len_surname)
