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
    'Digit 1 for Math Operations or Digit 2 for Temperature Conversion (°C->°F). Enter the mode: '))


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
        print(f'{temp_celsius} °C is egual to {temp_fahrenheit} °F')
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
#names += names1

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

#print(my_list, 'original')
# print(my_list.sort())
# print(sorted(my_list))
#print(my_list, 'new')

#print(my_dict, 'original')
#print(sorted(my_dict.values(), reverse=True))
#print(my_dict, 'new')

#print(my_list, 'original')
# print(list(reversed(my_list)))
#print(my_list, 'new')
# print(my_list[::1])  # copy
# print(my_list[::-1])  # reverse copy
my_llist = [['car', 4, 65], ['dog', 2, 30], ['bee', 1, 24]]
#print(sorted(my_list, key=abs))
print(sorted(my_llist, key=lambda item: item[1]))


# Dictionaries
movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John', 'Eric', 'Michael', 'George']
}
print(movie['title'])
#print(movie.get('budget', 'Not Found'))
movie['title'] = 'New Title'
movie['budget'] = 250000
print(movie['title'])
movie.pop('budget')
#del movie['budget']
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
            print(f'In Cart: {list(cart.keys())}. Total costs: {get_costs()} gold pieces. You have {get_money()} gold pieces yet.')
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
#print(list(zip(movies, year)))
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

"""

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
