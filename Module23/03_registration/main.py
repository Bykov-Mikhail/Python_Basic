def rule_check(list_line):
    if len(list_line) != 3:
        raise IndexError ("{line} НЕ присутствуют все три поля".format(line=list_line))
    if not list_line[0].isalpha():
        raise NameError ("{line} Поле «Имя» содержит НЕ только буквы".format(line=list_line))
    if '@' not in list_line[1] or "." not in list_line[1]:
        raise SyntaxError ("{line} Поле «Имейл» НЕ содержит @ (и/или) точку".format(line=list_line))
    if not (10 <= int(list_line[2]) <= 99):
        raise ValueError ("{line} Поле «Возраст» НЕ представляет число от 10 до 99".format(line=list_line))

def check_data(name_fail):
    with open(name_fail, 'r', encoding='utf-8') as reg_file, \
         open('registrations_good.log', 'a', encoding='utf-8') as good_file, \
         open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:

        for line in reg_file:
            list_data = []
            if line != '\n':
                list_data = line.split()
            try:
                rule_check(list_data)
                good_file.write(str(list_data) + "\n" * 2)
            except IndexError as exc:
                bad_file.write(str(exc) + "\n" * 2)
            except NameError as exc:
                bad_file.write(str(exc) + "\n" * 2)
            except SyntaxError as exc:
                bad_file.write(str(exc) + "\n" * 2)
            except ValueError as exc:
                bad_file.write(str(exc) + "\n" * 2)

check_data('registrations.txt')