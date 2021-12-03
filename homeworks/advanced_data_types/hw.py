int_a = 55 #1
print(id(int_a))
str_b = 'cursor'
print(id(str_b))
set_c = {1, 2, 3}
print(id(set_c))
lst_d = [1, 2, 3]
print(id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))
lst_d = lst_d + [4, 5] #2
print(lst_d)
print(id(lst_d))
print(type(int_a)) #3
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))
print(isinstance(int_a, int)) #4
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))
print("Anna has {} apples and {} peaches.".format(4, 2)) #5
print("Anna has {0} apples and {1} peaches.".format("red", 6)) #6
print("Anna has {t} apples and {s} peaches.".format(t = "tasty", s = "sweet")) #7
print("Anna has {0:5} apples and {1:9} peaches.".format(7, "sweet")) #8
num1 = 3
word = "red"
print(f"Anna has {num1} apples and {word} peaches.") #9
num1 = 3
word = "red"
print(f"Anna has %d apples and %s peaches." % (num1, word)) #10
h_dict = {"color": word, "number": num1}
print("Anna has %(number)d apples and %(color)s peaches." % h_dict)  #11

# Comprehensions
# (1)
list_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)] #12
print(list_comp)
# (2)
lsm = []
for num in range(10):
    if num % 2 == 0:
        lsm.append(num // 2)
    else:
        lsm.append(num * 10)
print(lsm) #13
# (3)
dict_com = {num : num ** 2 for num in range(1, 11) if num % 2 == 1} #14
print(dict_com) #14
# (4)
dict_com1 = {num : num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_com1) #15
# (5)
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print(d) #16
# (6)
d1 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d1[x] = x ** 3
    else:
        d1[x] = x
print(d1) #17

#Lambda
# (7)
foo = lambda x, y: x if x < y else y #18
print(foo(5,7))
# (8)
def foo(x, y, z): #19
    if y < x and x > y:
        return z
    else:
        return y
print(foo(51, 87, 22))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort)) #20
print(sorted(lst_to_sort, reverse=True)) #21
mult_lst = list(map(lambda x : x * 2, lst_to_sort)) #22
print(mult_lst)
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_new = list(map(lambda x, y: x ** y, list_A, list_B)) #23
import functools
comp = (lambda x, y: x + y)
functools.reduce(comp, lst_to_sort) #24
lst_neu = list(filter(lambda x: (x % 2 == 1), lst_to_sort )) #25
print(lst_neu)

lst_neg = list(filter(lambda b: b < 0, range(-10, 10))) #26
print(lst_neg)

list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_3 = list(filter(lambda x: x in list_1, list_2)) #27
print(list_3)





