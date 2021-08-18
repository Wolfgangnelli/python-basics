"""
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

"""
name = 'TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg1)
