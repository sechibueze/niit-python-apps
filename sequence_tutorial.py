
# fruits = ['apple', 'paw-paw', 'orange', 'mango']
#
# print('Fruits: {}'.format(fruits))
# print(len(fruits))
#
# print(fruits[2])
# fruits[2] = 'Cucumber'
# print('Fruits after: {}'.format(fruits))
#
# print(fruits[::-1])
# print(fruits[2:])
# print(fruits[:2])
# fav_fruits = []
# for fruit in fruits:
#     fav_fruits.append(fruit)
# print(fav_fruits)
# print(fav_fruits.insert(0, "Carrot"))
# fav_fruits.extend(fruits)
# print(fav_fruits)

person = {
    "name": "Sam",
    "email": "sam@niit.com",
    "count": 45
}
time = {
    "1": "One",
    "2": "Two"
}
print(person)
person["address"] = "123 Sango"
print(person)
print(person.keys())
print(person.values())
print(person["name"])
print(person.get("phone", "090897567898"))

print(time)
person.update(time)
print(person)
