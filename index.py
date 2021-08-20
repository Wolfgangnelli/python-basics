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
"""
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
