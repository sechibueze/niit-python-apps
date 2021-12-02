# This program does add, subtract, multiply and divide
def add(x, y):
    return x + y
def subt(x, y):
    return x - y

options  = [
    "1: Add",
    "2: Subt",
    "3: Mult",
    "4: Div"
]
# a = 7
# b = 8
# print("Bolanle : {} years and Tinubu: {}".format(a, b))
for option in options:
    print(option)
operation = input("What do you want to do ")
first = float(input("Enter the first number "))
second = float(input("Enter the second number "))

if operation == '1':
    print("Added: {} + {} = {}".format(first, second, add(first, second)))
elif operation == '2':
    print("Subt ", 2)
else:
    print("No res")

