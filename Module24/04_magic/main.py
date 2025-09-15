class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()

    def __str__(self):
        return 'Вода'

class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()

    def __str__(self):
        return 'Огонь'

class Earth:
    def __str__(self):
        return 'Земля'


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()

    def __str__(self):
        return 'Воздух'

class Lava:
    def __str__(self):
        return 'Лава'

class Dust:
    def __str__(self):
        return 'Пыль'

class Lightning:
    def __str__(self):
        return 'Молния'

class Mud:
    def __str__(self):
        return 'Грязь'

class Steam:
    def __str__(self):
        return 'Пар'

class Storm:
    def __str__(self):
        return 'Шторм'

class Freez:
    def __add__(self, other):
        if isinstance(other, Water):
            return Ice()

class Ice:
    def __str__(self):
        return 'Лед'


water_elem = Water()
air_elem = Air()
fire_elem = Fire()
earth_elem = Earth()
freez_elem = Freez()


res_wind_water = water_elem + air_elem
res_water_fire = water_elem + fire_elem
res_water_earth = water_elem + earth_elem
res_air_fire = air_elem + fire_elem
res_air_earth = air_elem + earth_elem
res_fire_earth = fire_elem + earth_elem
res_freez_water = freez_elem + water_elem

print(res_wind_water, end='\n\n')
print(res_water_fire, end='\n\n')
print(res_water_earth, end='\n\n')
print(res_air_fire, end='\n\n')
print(res_air_earth, end='\n\n')
print(res_fire_earth, end='\n\n')
print(res_freez_water, end='\n\n')