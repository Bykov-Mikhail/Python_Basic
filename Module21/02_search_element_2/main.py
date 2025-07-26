site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(struct, key, deep = 0):
    if deep == 1 or deep == 0:
        if key in struct:
            return struct[key]

    if deep == 2 or deep == 0:
        for deep_key in struct.keys():
            find_key(struct[deep_key], key)
            if key in struct[deep_key]:
                return struct[deep_key][key]

    if not key in struct:
        return None

input_key = input("Введите искомый ключ: ")
answer = input("\nХотите ввести максимальную глубину? Y/N: ").lower()

if answer == "y":
    max_deep = int(input("\nВведите максимальную глубину: "))
    print("\nЗначение ключа:", find_key(site, input_key, deep = max_deep))
else:
    print("\nЗначение ключа:", find_key(site, input_key))