def read_file(name_file):
    file_num = open(name_file, 'r')
    sum_num = 0
    for line in file_num:
        numbers = line.split()
        for num in numbers:
            sum_num += int(num)
    file_num.close()

    return sum_num

sum_num = read_file('numbers.txt')

file_answer = open('answer.txt', 'w')
file_answer.write(str(sum_num))
file_answer.close()
