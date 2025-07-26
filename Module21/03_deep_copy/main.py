import copy
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def dev_site(struct, name):
    if not isinstance(struct, dict):
        return struct
    for key in struct.keys():
        dev_site(struct[key], name)
        if "title" in struct:
            struct["title"] = "Куплю/продам {name_prod} недорого".format(name_prod = name)
        if "h2" in struct:
            struct["h2"] = "У нас самая низкая цена на {name_prod}".format(name_prod = name)
    return {name : copy.deepcopy(struct)}


list_sites = []
quantity_sites = int(input("Сколько сайтов? "))

for num_iteration in range(1, quantity_sites + 1):
    name_product = input("\nВведите название продукта для нового сайта: ")
    if num_iteration == 1:
        print("\nСайт для {0}:".format(name_product))
        print("\n", dev_site(site, name_product))
        list_sites.append(dev_site(site, name_product))
    else:
        list_sites.append(dev_site(site, name_product))

for ready_sites in list_sites:
    for key, value in ready_sites.items():
        print("\nСайт для {0}:".format(key))
        print("\n", value)