"""
# Variables, Datatypes, Typecasting
failed_subjects = 2
name = "John"
is_going_to_party = False
a = int(1)
b = int("3")
c = float("1")
d = int(float("3.4"))
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' +
      str(failed_subjects) + ' subjects.')
name = "Eric"
print(name + ' will need to redo ' + str(failed_subjects) + ' courses.')
print(type('hello'))
print(type(2))
print(type(True))
print([a, b, c, d])

# Create appropriate Variables for Item name, the price
# and how many you have in stock
item_name = "product1"
price = 4.90
quantity = 10
print([{
    'Item_Name: ' + item_name,
    'Price: ' + str(price),
    'Quantity: ' + str(quantity)
}])


# Strings Basics / Slicing
msg = 'welcome to Python 101: Strings'
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(len(msg))
print(msg.count('o'))
# slicing
print(msg[11:18])


# Python 101: String Exercise 1
msg = "Welcome to Python 101: Strings"
new_msg = msg[-10] + ' ' + msg[:8] + msg[-5:-1] + \
    msg[7:11] + msg[8] + \
    msg[12] + msg[2] + msg[1] + msg[-5]
print(new_msg.title())
print(new_msg[::-1].title())


msg = "Welcome to Python 101: Strings"
print(msg.replace('Python', 'Javascript'))
print('Python' in msg)
print('Python' not in msg)

name = 'TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg1)

# User Input
name = input('What is your name?: ')
age = input('What is your age?: ')
print(f'Hello {name}! You are {age} years old.')

num1 = input('Enter a digit: ')
num2 = input('Enter a second number: ')
answer = float(num1)+float(num2)
print(answer)

# User Input Exercise
first_name = input('Enter your name: ')
distance_km = float(input('Enter the distance in km: '))
distance_miles = round(distance_km / 1.609, 1)
print(f'Hi {first_name.capitalize()}! The distances are: {distance_km} km and {distance_miles} miles')

# Lists
friends = ['John', 'Mario', 'Franco', 'Guido']
print(friends[0], friends[2])
print(friends[:2])
print(len(friends))
print(friends.index('Mario'))

friends = ['John', 'Marco', 'Andrea', 'Massimo', 'Alessandro']
cars = [911, 130, 328, 535, 740, 308]
print(friends)

friends.sort()  # asc
print(friends)
friends.sort(reverse=True)  # desc
print(friends)
friends.reverse()
print(friends)
print(sum(cars))  # min() max() sum()


friends.insert(0, 'Francesco')  # append() insert()
# friends.extend(cars)
friends.remove('Francesco')
friends.pop(0)
# friends.clear()
# del friends
new_friends = friends[:]
# or friends.copy() or list(friends)   ways for copy list
print(friends)
print(new_friends)

# Lists - Exercise - Selling lemonade
sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []

last_day_w2 = int(input('How many lemonade today?: '))
sales_w2.append(last_day_w2)
sales = sales_w1 + sales_w2
# sales.extend(sales_w1)
# sales.extend(sales_w2)
sales.sort()
profit_tot = sum(sales) * 1.5
best_day = sales[-1] * 1.5
worst_day = sales[0] * 1.5
print(f'The total profit is: {profit_tot}$')
print(f'The best day i have earned {best_day}$')
print(f'The worst day i have earned only {worst_day}$')

# Split - Join
msg = 'Welcome to Python 101: Split and Join'
csv = 'Eric, John, Michael, Terry,Graham'
friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']
print(msg.split())  # csv.split(',')
print('-'.join(friends_list))
print('-'.join(msg.split()))
print(msg.replace(' ', ''))

# Split - Join Exercise
csv = 'Eric,John,Michael,Terry,Graham:TerrG;Brian'
friends_list = ['Exercise: fill me with names']

friends_list = print(','.join(','.join(csv.split(';')).split(':')).split(','))
# csv.replace(';', ',').replace(':', ',').split(',')
print(friends_list)

# Tuples
friends_tuple = ('Jhon', 'Terry', 'Eric')

# Sets
friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Eric', 'Graham'}
my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}

print(friends_set.intersection(my_friends_set))  # .difference .union
# Sets - Exercises
friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
cars = ['900', '420', 'V70', '911', '996',
        'V90', '911', '911', 'S', '328', '900']

# 1. Check if 'Eric' and 'John' exist in friends
print('Eric' in friends and 'John' in friends)
# 2. Comnbine or add the two sets
print(friends.union(my_friends))
print(friends | my_friends)
# 3. Find names that are in both sets
print(friends.intersection(my_friends))
print(friends & my_friends)
# 4. Find names that are only in friends
print(friends.difference(my_friends))
print(friends - my_friends)
# 5. Show only the names who only appear in one of the lists
print((friends - my_friends).union(my_friends - friends))
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)
# 6. Create a new cars-list without duplicates
cars_no_dupl = list(set(cars))
print(cars_no_dupl)

# Functions - Calling,Parameters,Args,Default


def greeting(name, age="20", color='red'):
    print(
        f'Hello {name.capitalize()}, you will be {str(age+1)} years old next birthday!')
    print(
        f'We hear you like the color {color.lower()}!')


name = input("Enter your name: ")
age = int(input('Enter your age: '))
color = input('Your color is: ')
greeting(name, age, color)

# Functions - Named Notation
greeting(age=50, color='blue', name='Mario')

# Return statements


def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    # [..., ..., ...]  or {..., ..., ...} or f"{...}, {...}, {...}"
    return amount, tax, total_amount


price = value_added_tax(100)
print(price, type(price))

# Comparisons and Booleans
a = [3, 7, 42]
b = a
print(id(a), id(b))
print('o' in 'John')
print('John' is not 'John')

# Conditionals
is_raining = False
is_could = True
print('Good Morning')
if is_raining and is_could:
    print('Bring Umbrella and jacket')
elif is_raining and not(is_could):
    print('Bring Umbrella')
elif not(is_raining) and is_could:
    print('Bring Jacket')
elif is_raining or is_could:
    print('Bring Umbrella or jacket')
else:
    print('Shirt is fine!')

amount = int(input('Enter the amount: '))
if amount <= 50:
    print('Purchase approved')
else:
    print('Please enter your pin!')


# If/Elif/Else - Exercise


def valid_mode(mode):
    modes = {'1', '2'}
    if mode not in modes:
        return False
    else:
        return int(mode)


mode = valid_mode(input(
    'Digit 1 for Math Operations or Digit 2 for Temperature Conversion (??C->??F). Enter the mode: '))


def valid_operator(operator):
    operators = {'-', '+', '*', '/'}
    if operator not in operators:
        return False
    else:
        return operator


if mode != False:
    if mode == 1:
        operator = valid_operator(input('Enter the operator (+,-,*,/): '))

        if operator == False:
            print('Invalid Operator!')
        else:
            val_1 = float(input('Enter first value: '))
            val_2 = float(input('Enter second value: '))

            if operator == '+':
                print(f'Result: {val_1+val_2}')
            elif operator == '-':
                print(f'Result: {val_1-val_2}')
            elif operator == '*':
                print(f'Result: {val_1*val_2}')
            elif operator == '/':
                print(f'Result: {val_1/val_2}')
    elif mode == 2:
        temp_celsius = float(
            input('Enter Celsius, for float number use point (ex. 20.5): '))
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        print(f'{temp_celsius} ??C is egual to {temp_fahrenheit} ??F')
    else:
        print('Wrong digit!')
else:
    print('Invalid mode!')


# Conditionals - Exercise improve

def num_days(month):
    days = 31
    if month in {'apr', 'jun', 'sep', 'nov'}:
        days = 30
    elif month == 'feb':
        days = 28
    print(f'number of days in {month} is {days}')


def valid_month(value):
    months = {'jan', 'feb', 'mar', 'apr', 'may', 'jun',
              'jul', 'aug', 'sep', 'oct', 'nov', 'dec'}
    if value not in months:
        return False
    else:
        return value


month = valid_month(input(
    'Enter a shortened month (jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec): '))

if month == False:
    print('Invalid month')
else:
    num_days(month)

# While Loops
index = 1
str_num = 5
while index <= str_num:
    print(f'{index}.'+'*'*index+'Loops are great'+'*'*index)
    index += 1


# While Loops - Exercise
print('******** GUESSING GAME !!! ********')

win_number = 22
is_winner = False
attempts = 3
i = 1


def is_between(value):
    return 1 <= value <= 100


def check_num(num):
    if num == win_number:
        return True
    else:
        return False


def tip(num):
    if num > win_number:
        print('Your number is too high')
    elif num < win_number:
        print('Your number is too low')


while i <= attempts:
    num = int(input(f'{i}.Attempt - Guess the number (between 1 and 100): '))
    if is_between(num) == False and i <= 1:
        print('WAKE UP! READ! The number must be between 1 and 100!')
        i += 1
    elif is_between(num) == False and i == 2:
        print('What kind of problems do you have? READ THE INSTRUCTIONS! The number MUST be between 1 and 100 !')
        i += 1
    elif is_between(num) == False and i > 2:
        print('You are banned from this game...RIP')
        break
    elif is_between(num) == True:
        is_winner = check_num(num)
        if is_winner == True:
            print('Congraturations, you have WON!!')
            break
        elif is_winner == False:
            if i == 3:
                print('You lost... TRY AGAIN!')
                break
            else:
                tip(num)
                i += 1

# For Loops - Nesting
friends = ['John', 'Terry', 'Eric']
values = [1, 2, 3]

for friend in friends:
    for value in values:
        print(f'{value}. {friend}')

else:
    print('End of the loop!')

# For Loops - Exercise - Party Invitation
names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'You are invited to the party on saturday.'

names.extend(names1)
# names += names1

for val in range(2):
    names.append(input('Enter the name of your friend: '))

for name in names:
    print(f'{name.lower().title()}! {msg}')


# Enumerate This!
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

for num, friend in enumerate(friends, 1):
    print(num, friend)

for friend in enumerate(enumerate(friends, 50), -100):
    print(friend)


# Sort - Sorted
my_list = [1, 5, -3, 7, -2]
my_dict = {'car': 4, 'dog': 2, 'add': 3, 'bee': 1}
my_tuple = ('d', 'c', 'e', 'a', 'b')
my_string = 'python'

# print(my_list, 'original')
# print(my_list.sort())
# print(sorted(my_list))
# print(my_list, 'new')

# print(my_dict, 'original')
# print(sorted(my_dict.values(), reverse=True))
# print(my_dict, 'new')

# print(my_list, 'original')
# print(list(reversed(my_list)))
# print(my_list, 'new')
# print(my_list[::1])  # copy
# print(my_list[::-1])  # reverse copy
my_llist = [['car', 4, 65], ['dog', 2, 30], ['bee', 1, 24]]
# print(sorted(my_list, key=abs))
print(sorted(my_llist, key=lambda item: item[1]))


# Dictionaries
movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John', 'Eric', 'Michael', 'George']
}
print(movie['title'])
# print(movie.get('budget', 'Not Found'))
movie['title'] = 'New Title'
movie['budget'] = 250000
print(movie['title'])
movie.pop('budget')
# del movie['budget']
print(movie)
for key, value in movie.items():
    print(key, value)


# Dictionaries II
python = {'Jogn': 35, 'Eric': 36, 'Michael': 35,
          'Terry': 38, 'Graham': 37, 'TerryG': 34}
holy_grail = {'Arthur': 40, 'Galahad': 35,
              'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}
life_of_brian = {'Brian': 33, 'Reg': 35,
                 'Stan/Loretta': 32, 'Biccus Diccus': 45}

people = {}
people1 = {}
people2 = {}
# method 1 update
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(sorted(people.items()))
# method 2 comprehension
for groups in (python, holy_grail, life_of_brian):
    people1.update(groups)
print(sorted(people1.items()))
# method 3 unpacking 3.5 later
people2 = {**python, **holy_grail, **life_of_brian}
print(sorted(people2.items()))
print('The sum of the ages: ', sum(people.values()))


# Dictionaries exercise

# The stores
freelancers = {'name': 'freelancing Shop', 'brian': 70, 'black knight': 20,
               'biccus diccus': 100, 'grim reaper': 500, 'minstrel': -15}
antiques = {'name': 'Antique Shop', 'french castle': 400,
            'wooden grail': 3, 'scythe': 150, 'catapult': 75, 'german joke': 5}
pet_shop = {'name': 'Pet Shop', 'blue parrot': 10,
            'white rabbit': 5, 'newt': 2}

# Initial inventory
department_store = {}
for department in (freelancers, antiques, pet_shop):
    department_store.update(department)

department_store.pop('name')
print(f'Initial inventory of stores: {sorted(department_store.items())}')
print('--------------------')

def show_list_items(shops):
    i = 0
    list_items = {}
    for name, value in shops.items():
        if i == 0:
            i += 1
            continue
        else:
            list_items.update({name: value})
            i += 1
    return list_items


def list_to_string(s):
    return (", ".join(s))

costs = []
def set_costs(cost):
    costs.append(cost)

def get_costs():
    return sum(costs)

def get_money():
    my_money = 1000
    my_money -= sum(costs)
    return my_money

def check_money(cost):
    have_money = get_money() >= cost
    if have_money == True:
        set_costs(cost)
    return have_money


cart = {}
valid_input = True
for shop in (freelancers, antiques, pet_shop):
    items = show_list_items(shop)
    buy_item = input(
        f'Welcome to {shop["name"]}! What do you want to buy {items}, or digit "exit": ').lower()
    if buy_item == 'exit':
        continue
    elif buy_item not in shop.keys():
        print('Enter a valid item!')
        valid_input = False
        continue
    else:
        item_value = shop[buy_item]
        money_available = check_money(item_value)
        if money_available == True:
            shop.pop(buy_item)
            cart.update({buy_item.capitalize(): item_value})
            print(
                f'In Cart: {list(cart.keys())}. Total costs: {get_costs()} gold pieces. You have {get_money()} gold pieces yet.')
if valid_input == True:
    print(
        f'You Purchased {list_to_string(list(cart.keys()))}. PAYMENTS: {get_costs()}, BALANCE: {get_money()}. Have a nice day of mayhem!')

print('--------------------')
department_store_final = {**freelancers,**antiques, **pet_shop}
department_store_final.pop('name')
print(f'Final Inventory of stores: {sorted(department_store_final.items())}')

# Exceptions: Try/Except, Raise

try:
    num = int(input('Enter a number between 1 and 30: '))
    num1 = 30/num
    if num > 30 or num < 1:
        raise ValueError(num)
except ZeroDivisionError as err:
    print(err, 'You can\'t divide by Zero!')
except ValueError as err:
    print(err, 'The value must be an integer and between 1 and 30!')
except:
    print('Invalid Input!')
else:
    print(f'30 divided by {num} is: {30/num}')
finally:
    print('**Thank you for playing!**')



# Classes & Objects

class Movie:

    def __init__(self, title, year, imbd_score, have_seen):
        self.title = title
        self.year = year
        self.imbd_score = imbd_score
        self.have_seen = have_seen

    def movie_card(self):
        print(f'Title: {self.title}')
        print(f'Year of production: {self.year}')
        print(f'IMDB Score: {self.imbd_score}')
        print(f'I have seen it: {self.have_seen}')


movie_1 = Movie('Transformer', 2007, 8.2, True)
movie_1.movie_card()


# Inheritance
class Person:
    def move(self):
        print('Moves 4 paces')

    def rest(self):
        print('Gains 4 health points')


class Doctor(Person):
    def heal(self):
        print('Heals 10 health points')


class Fighter(Person):

    def figth(self):
        print('Do 10 health points of damage')

    def move(self):
        print('Moves 6 paces')


class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print('Turns invisible')

    def heal(self):
        print('Heals 15 health points')


character_1 = Wizard()
character_1.move()


# Modules

# import platform as pl
from platform import python_version as pv

print(pv())


# Zip / Unzip

nums = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']
names = ['John', 'Eric', 'Michael', 'Graham', 'Joe']

# zip (packing)
combo = list(zip(nums, letters, names))
print(combo)

# unzip (unpacking)
num, let, nam = zip(*combo)
print(num, let, nam)

keys = 'this parrot is deceased'
values = 'denna papegoian ar avliden'
keys = keys.split()
values = values.split()
print(keys, values)
en_sv_dict = dict(zip(keys, values))
print(en_sv_dict)
new_dict = {key: value for key, value in zip(keys, values)}
print(new_dict)
en, sv = list(en_sv_dict.keys()), list(en_sv_dict.values())
print(en, sv)
en_1, sv_1 = zip(*en_sv_dict.items())
print(en_1, sv_1)



# Lambda Functions part 1

monty_python = ['John Marwood Cleese', 'Eric Idle', 'Michael Edward Palin',
                'Terrence Vance Gilliam', 'Terry Graham Perry Jones', 'Graham Arthur Chapman']

monty_python.sort(key=lambda name: name.split(' '))
print(monty_python)

# Lambda Functions part 2


def func(n):
    return lambda a: a*n


func2 = func(5)
print(func2(5))


def price_calc(start, hourly_rate):
    return lambda hours: start + hourly_rate * hours


walkin_cost = price_calc(10, 30)
premiun_cost = price_calc(1, 25)
print(walkin_cost(2))
print(premiun_cost(2))
print(price_calc(1, 25)(2))

print((lambda a, b, c: a+b+c)(2, 3, 4))
print((lambda *args: sum(args))(2, 3, 4, 50))

# Lambda Functions - Exercise

# 1
def f(x): return x + 5
# f = lambda x: x + 5
print(f(2))

# 2
def strip_spaces1(str): return ''.join(str.split(' '))
# strip_spaces1 = lambda str: ''.join(str.split(' '))
print(strip_spaces1('Monty Pythons Flying Circus'))

# 3
# join_list_no_duplicates = lambda list_a,list_b: list(set(list_a + list_b))
def join_list_no_duplicates(list_a, list_b):
    return list(set(list_a+list_b))

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6, 7]
print(join_list_no_duplicates(list_a, list_b))


# 4
def create_quad_fun(a, b, c):
    return lambda x: a*x**2 + b*x + c


f = create_quad_fun(2, 4, 6)
g = create_quad_fun(3, 5, 7)
print(f(2))
print(g(2))

# 5
signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups))  # Lexicographic sort
print(sorted(signups, key=lambda id: int(id[3:])))  # Integer sort

# 6
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

player_list.sort(key=lambda player: player.score, reverse=True)
print([player.name for player in player_list])

# Comprehensions - Lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num**2)
print(new_list)

new_list = [num*num for num in numbers]  # short hand
print(new_list)

# give me a list with num for each num in numbers if num is even
new_list = [num for num in numbers if num % 2 == 0]
print(new_list)

new_list = list(filter(lambda num: num % 2 == 0, numbers))
print(new_list)

# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list = []
for letter in 'spam':
    for num in range(4):
        new_list.append((letter, num))
print(new_list)

new_list = [(letter, num) for letter in 'spam' for num in range(4)]
print(new_list)



# Comprehensions - Dictionary
movies = ["And Now for Something Completely Different", "Monty Python and the Holy Grail", "Monty Python's Life of Brian",
          "Monty Python Live at the Hollywood Bowl", "Monty Python's The Meaning of Life", "Monty Python Live (Mostly)"]
year = [1971, 1975, 1979, 1982, 1983, 2014]
names = ['John', 'Eric', 'Michael', 'Graham', 'Terry', 'TerryG']
# print(list(zip(movies, year)))
# give me a dict('movies': year) for each movies, year in zip(movies, year)
new_dict = dict()
for movie, yr in zip(movies, year):
    new_dict[movie] = yr
# print(new_dict)
new_dict = {combo[0]: combo[1] for combo in list(zip(movies, year))}
# print(new_dict)
new_dict = {movie: yr for movie, yr in zip(
    movies, year) if yr < 1983 and movie.startswith('Monty')}
# print(new_dict)

n_1 = [[f"{name}'s favorite movie was '{movie}' from {str(yr)}"]
       for name, movie, yr in zip(names, movies, year) if yr < 1981]
print(n_1)


# Randomness
import random
import string
# for i in range(5):
#   print(random.random())

friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
# print(random.choice(friends_list))
# print(random.sample(friends_list, 2))

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

letters_numbers = string.ascii_letters + string.digits
print(letters_numbers)
# generate a secret code
code = ''
for i in range(12):
    code += random.choice(letters_numbers)
word1 = ''.join(random.sample(letters_numbers, 12))
word = ''.join(random.choices(letters_numbers, k=12))
print(code, word1, word)


# Timeit and performance
import timeit
print('Performance and timeit module')
# Experiment with sieve of Eratosthenes


def test1():
    [x for x in range(1, 151) if not any(
        [x % y == 0 for y in range(2, x)]) and not x == 1]
    return(1)


def test2():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]
    return(1)


def test3():
    primes = []
    for possiblePrime in range(2, 151):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return(1)


print(timeit.timeit('test1()', globals=globals(), number=10))
print(timeit.timeit('test2()', globals=globals(), number=10))
print(timeit.timeit('test3()', globals=globals(), number=10))


# Project - Crypto machine
print('Project - Crypto')


def enigma_ligth():
    # create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
# create two dictionaries
    dict_e = dict(zip(keys, values))
    dict_d = dict(zip(values, keys))
# OR create 1 and then flip
    # dict_e = dict(zip(keys, values))
    # dict_d = {value:key for key, value in dict_e.items()}
# user input 'the message' and mode
    msg = input('Enter the message: ')
    mode = input('Crypto mode: encode (e) OR decrypt as default: ')
# run encode or decode
    if mode.lower() == 'e':
        new_msg = [dict_e[letter] for letter in msg.lower()]
    else:
        new_msg = [dict_d[letter] for letter in msg.lower()]
# return result

    return ''.join(new_msg).capitalize()
# clean and beautify the code


print(enigma_ligth())




# Project Math Tutor
import random
import datetime

questions = []
answers = []
score = 0
times = []


def get_time_question(num):
    time = times[num][1] - times[num][0]
    return time


def time_each_question():
    for question in range(len(questions)):
        print(f'Time for {questions[question]}: {get_time_question(question)}')


def total_time():
    min_sec = []
    tot_min = 0
    tot_sec = 0
    for time in times:
        diff = time[1] - time[0]
        minutes = divmod(diff.seconds, 60)
        min_sec.append((minutes[0], minutes[1]))
    for val in min_sec:
        tot_min += val[0]
        tot_sec += val[1]
    if tot_sec >= 60:
        ms = tot_sec/60
        new_sec = ms % 1
        new_min = ms // 1
        tot_min += new_min
        tot_sec = new_sec
    print(f'Min: {tot_min}, Sec: {tot_sec}')


number_practice_questions = int(
    input('Enter the number of random practice questions: '))
max_n = int(input('Enter the max number used in practice: '))
for question in range(number_practice_questions):
    num1 = random.choice(range(1, max_n+1))
    num2 = random.choice(range(1, max_n+1))
    questions.append(f'{num1} * {num2}')
    time_start = datetime.datetime.now()
    answer = input(f'{num1} x {num2} = ')
    if len(answer) > 0:
        time_stop = datetime.datetime.now()  # .strftime("%X")
        times.append((time_start, time_stop))
    answers.append(int(answer))
    correct_answer = num1*num2
    if int(answer) == correct_answer:
        score += 1
print(
    'Thanks for playing with Multiplication tables! \nCorrect answer: {score} \nTotal answer: {number_practice_questions}')
print(f'% of correct answer: {round(score/number_practice_questions)*100}%')
print('Time for each question: ')
time_each_question()
print(f'Total time for all questions: ')
total_time()
i = 0
for q in questions:
    print(f'{q} = {answers[i]}')
    i += 1

'''
# COME LO HA FATTO LUI

# import modules
# ask how many questions user wants
from random import randrange as r
from time import time as t
no_questions = int(input("How many questions do you want?: "))
max_num = int(input('Highest number used in practice?: '))

# set score start at zero
score = 0
answer_list = []
# loop through number of questions
start = t()
for q in range(no_questions):
    # create two random numbers and calc answer
    num1, num2 = r(1, max_num+1), r(1, max_num+1)
    ans = num1*num2
# show user the question
# capture answer and modify user score
    u_ans = int(input(f'{num1} x {num2} = '))
    answer_list.append(f'{num1} x {num2} = {ans} you:{u_ans}')
    if u_ans == ans:
        score += 1
    end = t()
# output final score
print(
    f'Thank you for playing! \nYou got {score} out of {no_questions} ({round(score/no_questions)*100}%) correct in {round(end-start,1)} seconds ({round((end-start)/no_questions,1)} seconds/question)')
for a in answer_list:
    print(a)
'''


# Project - Marble/Trading game

import random

green_marbles_bag = []
red_marbles_bag = []
money = 1000
start_rounds = 1

for num in range(1, 6):
    green_marbles_bag.append(f'green_{num}')

for num in range(1, 4):
    red_marbles_bag.append(f'red_{num}')

marbles_bag = ['black_10', 'white_5']
marbles_bag.extend(green_marbles_bag)
marbles_bag.extend(red_marbles_bag)

print('Welcome to Trading Game Simulation \nYour budget is 1000$ !')
total_rounds = random.randrange(start_rounds+1, 10)
for round in range(start_rounds, total_rounds+1):
    bet = int(input(f'Current Money: {money}$. How much you will bet?: '))
    if bet <= money and money > money/2:
        murble = random.choice(marbles_bag)
        murble_split = murble.split('_')
        if murble_split[0] == 'green':
            print(f'You have draw {murble}! You have WON {bet}$')
            money += bet
        elif murble_split[0] == 'red':
            print(f'You have draw {murble}. You have LOSE {bet}$')
            money -= bet
        elif murble_split[0] == 'black':
            print(
                f'WOW! You have draw {murble}. You have WON {murble_split[1]} x {bet} = {bet*10}$')
            money += bet*10
        elif murble_split[0] == 'white':
            print(
                f'OH NO! sYou have draw {murble}. You have LOSE {murble_split[1]} x {bet} = -{bet*5}$')
            money -= bet*5
    elif bet > money and money > money/2:
        print(f'You don\'t bet {bet}$, your remained budget is {money}$')
        continue
    elif money < money/2:
        print('Sorry! You have lose half of your money... Game is over!')
        break
    print(f'Round number: {round}/{total_rounds} \nMoney: {money}$')


# COME LO HA FATTO LUI
'''
bag = ('green', 'green', 'green', 'green', 'green',
       'green', 'red', 'red', 'red', 'red')
start_purse = 1000
purse = start_purse
result = 0
rounds = 3
marble = 'none'

print(f'You start the game with {start_purse} gold pieces')

for draw in range(1, rounds+1):
    bet = int(input(
        f'Current Purse: {purse} Last draw: {marble} \nRound {draw} - How much do you want to bet?: '))
    marble = random.choice(bag)
    if marble == 'green':
        result = bet
    elif marble == 'black':
        result = 10 * bet
    elif marble == 'white':
        result = -5 * bet
    else:
        result = -bet

    purse += result
    if purse < (0.5 * start_purse):
        print(f'Game over! You lost to much gold!!')
        break
    print(f'purse: {purse}, last result: ({marble}): {result}')
    print('')
print('starting/ending purse: ', start_purse, '/', purse)
print('gain/loss: ', ((purse-start_purse)/start_purse*100), '%')
'''


# Project Euler Q4 - Palindromes
import time


def is_palindrome(val):
    val = str(val)
    if val == val[::-1]:
        return True
    else:
        return False
# def is_palindrome(val):
#    return str(val) == str(val)[::-1]


def palindrome():
    start_time = time.time()
    palindromes_list = []
    debug_list = []
    low_val = 900
    high_val = 999
    interations = 0

    for num1 in range(low_val, high_val):
        for num2 in range(low_val, high_val):
            interations += 1
            if is_palindrome(num1*num2):
                palindromes_list.append(num1*num2)
                debug_list.append([num1, num2, num1*num2])
            if num1 == num2:
                break
    print('print of palindromes: ', palindromes_list, num1, num2)
    print('debug_list: ', debug_list)
    print('Interations: ', interations)
    print('Largest palindrome: ', max(palindromes_list))
    print('Runtime: ', time.time()-start_time)
    print('-----------------End Run----------------')


def palindrome_back():
    start_time = time.time()
    palindromes_list = []
    debug_list = []
    low_val = 900
    high_val = 999
    interations = 0
    low_num2_val = 900

    for num1 in range(high_val, low_val, -1):
        if num1 < low_val:
            break
        for num2 in range(high_val, low_num2_val, -1):
            interations += 1
            if is_palindrome(num1*num2):
                palindromes_list.append(num1*num2)
                low_val = max((num1*num2)/high_val, low_val)
                low_num2_val = num2
                debug_list.append([num1, num2, (num1*num2)/high_val, low_val])
            if num1 == num2:
                break
    print('print of palindromes: ', palindromes_list, num1, num2)
    print('debug_list: ', debug_list)
    print('Interations: ', interations)
    print('Largest palindrome: ', max(palindromes_list))
    print('Runtime: ', time.time()-start_time)
    print('-----------------End Run----------------')


palindrome()
palindrome_back()



# Scrivi la tua versione di len()

def my_len(str_or_lst):
    length = 0
    for unit in str_or_lst:
        length += 1
    return length


print(my_len('test my len'))



# Histograms Generator

# version 1
def histogram(num_lst):
    output = ""
    for item in num_lst:
        for num in range(item):
            output += '*'
        output += '\n'
    return output

# verion 2
def istogramma(list):
    for num in list:
        print('*'*num)


arr = [3, 7, 9, 5]
print(histogram(arr))
istogramma(arr)


# A ciascuno il suo

# versione 1
def char_counter(str_list):
    num_list = []
    for item in str_list:
        num_list.append(len(item))
    return num_list

# version 2
def char_counter_pro(str_list):
    return [len(item) for item in str_list]


list_str = ['minni', 'bell', 'bebidina']
print(char_counter(list_str))
print(char_counter_pro(list_str))


# Frequency Meter


def frequency_meter(string):
    frequency_dict = {}
    for letter in string:
        if letter in frequency_dict:
            # frequency_dict[letter] += 1
            frequency_dict.update({letter: frequency_dict[letter]+1})
        else:
            frequency_dict[letter] = 1
    return frequency_dict


print(frequency_meter('ababcc'))


# Only Members


def only_members(item, items_list):
    msg = f"No {item} isn't in the list"
    if item.capitalize() in items_list:
        msg = f'Yes {item} is in the list and his index is {items_list.index(item)}'
    return print(msg)


list_itm = ['Marco', 'Franco', 'Andrea', 'Mario', 'Alessandro']
only_members('Mario', list_itm)


# Il linguaggio dei furfanti n.14

def traduttore():
    print('Ciao! Questo programma traduce un testo passato in "rovarspraket".\nSignifica che raddoppia ogni consonante delle parole e ci mette una "o" in mezzo...')
    consonants = 'b,c,d,f,g,h,l,m,n,p,q,r,s,t,v,z'

    while True:
        new_phrase = ''
        text = str(input('Inserisci il testo che vuoi tradurre: '))

        for letter in text:
            if letter in consonants:
                new_phrase += letter+'o'+letter
            else:
                new_phrase += letter
        print(f'Frase tradotta: {new_phrase}')

        if str(input('\nVuoi tradurre un\'altra frase (y/n)? ')) == 'n':
            break


traduttore()


# The Surveyor
def calc_area(figure):
    area = 0
    if figure == 'cerchio':
        radius = float(input('Valore raggio? '))
        area += 3.14 * (radius**2)
    elif figure == 'quadrato':
        lato = float(input('Valore lato: '))
        area += lato**2
    elif figure == 'rettangolo':
        base = float(input('Valore base: '))
        altezza = float(input('Valore altezza: '))
        area += (base*altezza)
    elif figure == 'triangolo':
        base = float(input('Valore base: '))
        altezza = float(input('Valore altezza: '))
        area += (base*altezza)/2
    if area != 0:
        return print(f'L\'area del {figure} ?? {str(area)}')
    else:
        return print('Non ?? possibile effettuare calcoli per la figura inserita')


fig = input(
    'Di quale figura vuoi calcolare l\'area? (cerchio, quadrato, rettangolo, triangolo): ')
calc_area(fig.lower())


# L'Americana


def converter():
    print('Hey! This function convert your meter value into miles, yards, feet and inches!')
    user_meter_value = float(input('Please, enter the value in METER: '))
    values = {}
    for i in range(4):
        if i == 0:
            values['miles'] = (user_meter_value/1609.334)
        elif i == 1:
            values['yards'] = (user_meter_value*1.0936133)
        elif i == 2:
            values['feet'] = (user_meter_value*3.28084)
        elif i == 3:
            values['inches'] = (user_meter_value*39.3701)
    for key in values.keys():
        print(f'\n{key}: {values[key]}')


converter()


# The lord of time


def lord_of_time():
    print('Hey! This function convert days, hours and minutes in seconds!')
    from_days = int(input('Number of days: ')) * 24 * 3600
    from_hours = int(input('Number of hours: ')) * 3600
    from_minutes = int(input('Number of minutes: ')) * 60
    print(f'Total Seconds: {from_days+from_hours+from_minutes}')


lord_of_time()


# Password Generator
import string
import random
import secrets


def generate_password():
    characters_list = string.ascii_letters + string.digits
    _password = []
    print('Hey! This function generate a random passwords!')
    password_type = int(input(
        'Digita il numero 1 o 2 in base al tipo di password che desideri:\nComplessa (1)\nSemplice (2) \n'))
    if password_type == 1:
        for i in range(20):
            _password.append(random.choice(characters_list))
        _password = "".join(_password)
        print(f'Random Password: {_password}')
    elif password_type == 2:
        for i in range(8):
            _password.append(random.choice(characters_list))
        _password = "".join(_password)
        print(f'Random Password: {_password}')
    else:
        print('Error! The value is wrong! Enter 1 or 2')


def psw_generator_pro():
    print('Il programma permette di scegliere tra due livelli di complessit?? della password.')

    ascii_chars = string.digits + string.ascii_letters + string.punctuation
    alphanum_chars = string.digits + string.ascii_letters

    if input('Desideri una password Semplice o Complessa? S/C ').upper() == 'C':
        lunghezza = 20
        tipo = ascii_chars
    else:
        lunghezza = 8
        tipo = alphanum_chars

    psw = "".join(secrets.choice(tipo) for _ in range(lunghezza))
    print(f'La password generate ??: {psw}')


psw_generator_pro()

# Funzione genera mac
import string
import random


def genera_mac():
    ascii_char = string.ascii_lowercase + string.ascii_uppercase
    random_char = random.choices(ascii_char, k=6)
    indirizzo = ":".join("{0:X}".format(ord(c)) for c in random_char)
    print(indirizzo)


genera_mac()


def generate_mac():
    char_set = string.digits + 'ABCDEF'
    mac_addr = ''
    points = 0

    for _ in range(6):
        for _ in range(2):
            mac_addr += random.choice(char_set)
        if points < 5:
            mac_addr += ':'
            points += 1
    return mac_addr


print(generate_mac())

# Write a py function that takes a sequence of numbers and determines whether all the numbers are different from each other.


def is_different_numbers():
    num_seq = []
    for _ in range(10):
        num = int(input(f'Enter the {_+1}?? integer number: '))
        num_seq.append(num)
    if len(num_seq) == len(set(num_seq)):
        print('All numbers are different!')
    else:
        print('There are equal numbers!')


is_different_numbers()

# Write a py program to create all possible strings by using a,e,i,o,u. Use the characters excatly once.
from itertools import permutations


def possible_string():
    chars = list('aeiou')
    permutations_list = list(permutations(chars))
    new_list = [''.join(list(p)) for p in permutations_list]
    for s in new_list:
        print(f'{s}, ')


possible_string()

# Python Basic (Part-II) 47. Write a py program which readds a text (only alphabetical characters and spaces) and prints two words. The first one is the word which is arise most frequently in the text.
# The second one is the word which has the maximum number of letters.

import collections

print('Input a text in a line')
text_list = list(map(str, input().split()))
sc = collections.Counter(text_list)
common_word = sc.most_common()[0][0]
common_word_num = sc.most_common()[0][1]
max_char = ''
for s in text_list:
    if len(max_char) < len(s):
        max_char = s
print(
    f'Most frequent word: {common_word} ({common_word_num})\nWord with max number of letters: {max_char}')


# Write a py program to find common divisors between two numbers in a given pair.


def ngcd(x, y):
    i = 1
    while i <= x and i <= y:
        if x % i == 0 and y % i == 0:
            gcd = i
        i += 1
    return gcd


def num_common_div(x, y):
    n = ngcd(x, y)
    result = 0
    z = int(n**0.5)
    i = 1
    while i <= z:
        if n % i == 0:
            result += 2
            if i == n/i:
                result -= 1
        i += 1
    return result


print(num_common_div(12, 24))

# Write a Python program to reverse only the vowels of a given string


def reverse_vowels(str1):
    vowels = ''
    for char in str1:
        if char in 'aeiouAEIOU':
            vowels += char
    result_string = ''
    for char in str1:
        if char in 'aeiouAEIOU':
            result_string += vowels[-1]
            vowels = vowels[:-1]
        else:
            result_string += char
    return result_string


print(reverse_vowels('aeiou'))

# Module - types
import types
import copy

num_list = [1, [2, 3, 4]]
copy_list = copy.copy(num_list)


class C:
    def x():
        pass


def myFun():
    pass


print(isinstance(myFun, types.FunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance(C().x, types.MethodType))
print(copy_list)


# PYTHON DATA TYPE: STRING - EXERCISES

# 89. Write a py program to remove unwanted characters from a given string
import string

unwanted_characters = string.punctuation
given_string = input(
    'Write a string with some of this chars (<=>?@[\]^_`{|}~): ')
new_string = ''

# 1?? solution
for c in given_string:
    if c not in unwanted_characters:
        new_string += c

print(new_string)

# 2?? solution


def remove_chars(given_string):
    for c in unwanted_characters:
        given_string = given_string.replace(c, '')
    return given_string


print(remove_chars(given_string))

# 90. Write a py program to remove duplicate words from a given string

# 1?? solution


def remove_duplicate(str1):
    word_list = str1.split()
    no_duplicate_list = set(word_list)
    return ' '.join(no_duplicate_list)


print(remove_duplicate(input('Enter a string with duplicate words: ')))

# 2?? solution (best)


def unique_list(text_str):
    l = text_str.split()
    uniq = []
    for c in l:
        if c not in uniq:
            uniq.append(c)
    return ' '.join(uniq)


print(unique_list(input('Enter unother string with duplicate words: ')))

# 1. Write a py program to convert JSON data to Python obj --- DECODING JSON (Deserialize)
import json
'''
json_obj = '{"Name": "David", "Class": "I", "Age": 6}'
python_obj = json.loads(json_obj)
print('\nPython Object: ')
print(python_obj)
print('\nName: ', python_obj['Name'])
print('Class: ', python_obj['Class'])
print('Age: ', python_obj['Age'])
'''

# 2. Write a py program to convert Python obj to JSON data --- ENCODING PY OBJ (Serialize)
'''
py_obj = {'Name': 'David', 'Class': 'F', 'Age': 8}
json_data = json.dumps(py_obj)
print('JSON Data: ', json_data)
'''

# 4. Write a py program to convert Python dict obj (sort by key) to JSON dat. Print the obj members with indent level 4.
'''
py_dict = {'4': 5, '6': 7, '1': 3, '2': 4}
print('Original py obj: ')
print(py_dict)
print('\nJSON data: ')
print(json.dumps(py_dict, sort_keys=True, indent=4))

# 6. Write a py program to create a new JSON file from an existing JSON file.

with open('states.json') as f:
    state_obj = json.load(f)

for state in state_obj['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(state_obj, f, indent=2)

print(state_obj)

# 7. Write a py program to check whether an instance is complex or not.


def encode_complex(object):
    if isinstance(object, complex):
        return [object.real, object.imag]
    raise TypeError(repr(object) + ' is not JSON serialized')


complex_obj = json.dumps(2 + 3j, default=encode_complex)
print(complex_obj)
'''

# 9. Write a py program to access only unique key value of a Python object

json_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'

py_obj = json.loads(json_obj)
print(json_obj)


# PYTHON DATA TYPE: LIST - EXERCISES

# 1. Write a py program to sum all the items in a list

list_items = [2, 4, 2, 2]


def sum_list_items(list_):
    output = 0
    for item in list_:
        output += item
    return output


print(sum_list_items(list_items))

# 5. Write a py program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

test_list = ['abc', 'xyz', 'aba', '1221']

# solution 1


def check_same(l):
    new_list = []
    for i in l:
        if i[0] == i[-1]:
            new_list.append(i)
    return new_list


def check_len(l):
    new_list = []
    for i in l:
        if len(i) >= 2:
            new_list.append(i)
    return check_same(new_list)


print(len(check_len(test_list)))

# solution 2


def match_words_pro(l):
    cnt = 0
    for i in l:
        if len(i) >= 2 and i[0] == i[-1]:
            cnt += 1
    return cnt


print(match_words_pro(test_list))

# 6. Write a py program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

unordered_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def last(n): return n[-1]


def sort_list_last(tuples_list):
    return sorted(tuples_list, key=last)


print(sort_list_last(unordered_list))

# 7. Write a py program to remove duplicates from a list
_list = [2, 5, 98, 41, 2, 5, 5, 6]


def unique_value(a):
    dup_items = set()
    uniq_items = []
    for i in a:
        if i not in dup_items:
            uniq_items.append(i)
            dup_items.add(i)
    return uniq_items


print(unique_value(_list))

# 8. Write a py program to check a list is empty or not
_list = []


def is_empty(a):
    return True if not a else False


print(is_empty(_list))

# 9. Write a py program to clone or copy a list
_list = [2, 5, 98, 41, 2, 5, 5, 6]

print(_list.copy())

# 19. Write a py program to get the difference between the two lists
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 2, 9, 4, 7, 6]

# solution 1


def get_differences(a, b):
    list_3 = []
    for x in a:
        if x not in b:
            list_3.append(x)
    for y in b:
        if y not in a:
            list_3.append(y)

    return list_3


print(get_differences(list_1, list_2))

# solution 2
diff_list1_list2 = list(set(list_1) - set(list_2))
diff_list2_list1 = list(set(list_2) - set(list_1))
print(diff_list1_list2+diff_list2_list1)
"""

# 20. Write a py program access the index of a list
nums = [5, 8, 6, 4, 2]
for n_idx, n_val in enumerate(nums):
    print(n_idx, n_val)
