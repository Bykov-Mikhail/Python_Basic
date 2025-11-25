import requests
import json

"""Данные о корабле"""
req_starships = requests.get('https://www.swapi.tech/api/starships/12')

data_starships = json.loads(req_starships.text)

"""Данные о пилотах"""
req_pilot_1 = requests.get('https://www.swapi.tech/api/people/1')
req_pilot_2 = requests.get('https://www.swapi.tech/api/people/9')
req_pilot_3 = requests.get('https://www.swapi.tech/api/people/18')
req_pilot_4 = requests.get('https://www.swapi.tech/api/people/19')

data_pilot_1 = json.loads(req_pilot_1.text)
data_pilot_2 = json.loads(req_pilot_2.text)
data_pilot_3 = json.loads(req_pilot_3.text)
data_pilot_4 = json.loads(req_pilot_4.text)

"""Данные о планетах"""
req_pilot_1_2_home_name = requests.get('https://www.swapi.tech/api/planets/1')
req_pilot_3_home_name = requests.get('https://www.swapi.tech/api/planets/22')
req_pilot_4_home_name = requests.get('https://www.swapi.tech/api/planets/26')

data_name_planet_1 = json.loads(req_pilot_1_2_home_name.text)
data_name_planet_2 = json.loads(req_pilot_3_home_name.text)
data_name_planet_3 = json.loads(req_pilot_4_home_name.text)

"Приведение всех данных к требуемому формату"
name_planet_1 = [value for key , value in data_name_planet_1['result']['properties'].items() if key == 'name']
name_planet_2 = [value for key , value in data_name_planet_2['result']['properties'].items() if key == 'name']
name_planet_3 = [value for key , value in data_name_planet_3['result']['properties'].items() if key == 'name']

need_starships = {key : value for key, value in data_starships['result']['properties'].items() if key == 'max_atmosphering_speed' or key == 'name' or key == 'starship_class'}
need_pilots_1 = {key : value for key, value in data_pilot_1['result']['properties'].items() if key == 'height' or key == 'homeworld' or key == 'mass' or key == 'name'}
need_pilots_2 = {key : value for key, value in data_pilot_2['result']['properties'].items() if key == 'height' or key == 'homeworld' or key == 'mass' or key == 'name'}
need_pilots_3 = {key : value for key, value in data_pilot_3['result']['properties'].items() if key == 'height' or key == 'homeworld' or key == 'mass' or key == 'name'}
need_pilots_4 = {key : value for key, value in data_pilot_4['result']['properties'].items() if key == 'height' or key == 'homeworld' or key == 'mass' or key == 'name'}

need_pilots_1['homeworld_url'] = need_pilots_1.pop('homeworld')
need_pilots_2['homeworld_url'] = need_pilots_2.pop('homeworld')
need_pilots_3['homeworld_url'] = need_pilots_3.pop('homeworld')
need_pilots_4['homeworld_url'] = need_pilots_4.pop('homeworld')

need_pilots_1['homeworld'] = name_planet_1[0]
need_pilots_2['homeworld'] = name_planet_1[0]
need_pilots_3['homeworld'] = name_planet_2[0]
need_pilots_4['homeworld'] = name_planet_3[0]

need_starships['pilots'] = [need_pilots_1 , need_pilots_2, need_pilots_3, need_pilots_4]

with open('information', 'w') as file:
    json.dump(need_starships, file, indent=4)

print(need_starships)

