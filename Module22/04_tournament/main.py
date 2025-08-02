first_file = open('first_tour.txt', 'r')
list_first_tour = []
for line in first_file:
    elem = line.split()
    if elem != []:
        list_first_tour.append(elem)

list_win_first = []
for item in list_first_tour[1:]:
    if int(item[2]) > int(list_first_tour[0][0]):
        score = int(item[2])
        name = item[1][:1] + '.' + item[0] + ' ' + item[2] + '\n'
        list_win_first.append((score, name))

def key_sort(x):
    return x[0]

list_win_first.sort(key=key_sort, reverse=True)

result_lines = [line[1] for line in list_win_first]

second_file = open('second_tour.txt', 'w')

second_file.write(str(len(list_win_first)) + '\n' * 2)

for line in result_lines:
    second_file.write(line + '\n')

second_file.close()








