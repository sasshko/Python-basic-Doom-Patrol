# 1
class Laptop:
    def __init__(self):
        battery_t1 = Battery('For Acer')
        battery_t2 = Battery('For Dell')
        self.batteries = [battery_t1, battery_t2]


class Battery:
    def __init__(self, voltage):
        self.voltage = voltage


laptop = Laptop()
print(laptop.batteries[0].voltage)


# 2
class Guitar:
    def __init__(self, guitarstring):
        self.guitarstring = guitarstring


class GuitarString:
    def __init__(self):
        pass


guitarstring = GuitarString()
guitar = Guitar(guitarstring)


# 3
class Calc:
    @staticmethod
    def add_nums(a, b, c):
        return a + b + c


m = Calc()
print(m.add_nums(5, 6, 7))


# 4 video 37hv
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = [ingredients]

    def __repr__(self):
        return f'It consists of {self.ingredients}'

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta.carbonara()
pasta_2 = Pasta.bolognaise()
print(pasta_1)
print(pasta_2)


# 5
class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count):
        self.visitors_count = 0

    @property
    def visit_count(self):
        return self.visitors_count

    @visit_count.setter
    def visit_count(self, num):
        if num > self.max_visitors_num:
            self.visitors_count = self.max_visitors_num


Concert.max_visitor_num = 50
concert = Concert(1000)
concert.visitors_count = 1000
print(concert.visitors_count)

# 6
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


my_address = AddressBookDataClass(key=12, name='Bur',
                                  phone_number='44-658-65',
                                  address='Diagon',
                                  email='san@.com',
                                  birthday='11th Sep',
                                  age=21)
print(my_address)

# 7
from collections import namedtuple

AddressBookDataClass_1 = namedtuple('AddressBookDataClass',
                                    ['key', 'name',
                                     'phone_number',
                                     'address', 'email',
                                     'birthday', 'age'])

me_add = AddressBookDataClass_1(33, 'Mbur', '789-456',
                                'IF', 'mbur@.com',
                                '11.09', 21)
print(me_add)


# 8
class AddressBook:
    def __init__(self, key, name,
                 phone_number, address,
                 email, birthday, age):
        self.key = int(key)
        self.name = str(name)
        self.phone_number = str(phone_number)
        self.address = str(address)
        self.email = str(email)
        self.birthday = str(birthday)
        self.age = int(age)

    def __str__(self):
        return f'addbook {self.key}, {self.name}, \
               f {self.phone_number}, {self.address}, \
               f {self.email}, {self.birthday}, \
               f {self.age}'


adresa = AddressBook(key=22, name='meine',
                     phone_number='3515515',
                     address='bhbfjkds',
                     email='dbcdcd',
                     birthday='25oct',
                     age=23)
print(adresa)
print(adresa.name)


# 9
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def pr_age(self):
        return self.age

    @pr_age.setter
    def pr_age(self, new_age):
        self.age = new_age

    @pr_age.deleter
    def pr_age(self):
        del self.age


john = Person("John", 36, "USA")
john.pr_age = 37
print(john.pr_age)


# 10
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


bob = Student(0, 'Bob')

setattr(bob, 'student_email', 'bob4@.com')
print(getattr(bob, 'student_email'))


# 11
class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def print_temp(self):
        return self._temperature

    @print_temp.setter
    def print_temp(self, fahr):
        self._temperature = fahr


t = Celsius(32)
t.print_temp = t.print_temp * 1.8 + 32
print(t.print_temp)
