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


# 3 ?
class Calc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def add_nums(a, b, c):
        return a + b + c


m = Calc(5, 6, 7)
print(m.add_nums(5, 6, 7))


# 4 video 37hv
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = [ingredients]

    def carbonara(self):
        self.carbonara = ['tomatos, forcemeat']
        if self.carbonara == self.ingredients:
            return self.carbonara

    def bolognaise(self):
        self.bolognaise = ['bacon', 'parmesan', 'eggs']
        if self.bolognaise == self.ingredients:
            return self.bolognaise


pasta_1 = Pasta('bacon, parmesan, eggs')
print(pasta_1.bolognaise)


# 5
class Concert:
    def __init__(self, visitors_count):
        self.visitors_count = visitors_count

    def max_visitors_num(self):
        max_visitors_num = ()
        if self.visitors_count > max_visitors_num:
            return max_visitors_num == self.visitors_count


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

# 7
from collections import namedtuple

AddressBookDataClass = namedtuple('AddressBookDataClass',
                                  ['key', 'name',
                                   'phone_number',
                                   'address', 'email',
                                   'birthday', 'age'])


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

    def print_key(self):
        print('{self.key}')

    def print_name(self):
        print('{self.name}')

    def print_phone_number(self):
        print('{self.phone_number}')

    def print_adress(self):
        print('{self.address}')

    def print_email(self):
        print('{self.email}')

    def print_birthday(self):
        print('{self.birthday}')

    def print_age(self):
        print('{self.age}')


adresa = AddressBook(key=22, name='meine', phone_number='3515515', address='bhbfjkds', email='dbcdcd', birthday='25oct',
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


# 10 +
class Student:
    id = 0
    name = "Bob"


bob = Student()

setattr(bob, 'student_email', 'bob4@.com')
print(getattr(bob, 'student_email'))


# 11
class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def print_temp(self, ):
        fahr = self._temperature * 1.8 + 32
        return fahr
