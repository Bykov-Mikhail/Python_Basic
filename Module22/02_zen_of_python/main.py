def read_file(name_file):
    file_zen = open(name_file, 'r')
    list_text = []
    for line in file_zen:
        list_text.append(line)
    file_zen.close()
    return list_text

list_text = read_file('zen.txt')

for line in list_text[::-1]:
    if '\n' in line:
        print(line)
    else:
        print(line, '\n')
