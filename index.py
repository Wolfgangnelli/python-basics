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

"""
# Split - Join Exercise
csv = 'Eric,John,Michael,Terry,Graham:TerrG;Brian'
friends_list = ['Exercise: fill me with names']

friends_list = print(','.join(','.join(csv.split(';')).split(':')).split(','))
# csv.replace(';', ',').replace(':', ',').split(',')
print(friends_list)

# Tuples
friends_tuple = ('Jhon', 'Terry', 'Eric')
