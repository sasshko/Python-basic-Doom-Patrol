# 1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speeed = max_speed
        self.mileage = mileage


# 2
class Bus(Vehicle):

    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def print_seat(self):
        print(self.seating_capacity)


# 3
m = Bus(200, 20000, 32)
print(type(m))
# 4
print(isinstance(m, Vehicle))


# 5
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6
class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students,
                 max_speed, mileage, seating_capacity,
                 bus_school_color):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def print_col(self):
        print(f'Bus is {self.bus_school_color}')


# 7
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f'Bear says {self.sound}')


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f'Wolf says {self.sound}')


bear = Bear("Rrrr")
wolf = Wolf("Auuu")
anim = (bear, wolf)

for sounds in anim:
    print(sounds.make_sound())


# 8
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        new_instance = super(City, cls).__new__(cls)
        if population > 1500:
            return new_instance
        else:
            print("Your city is too small")
