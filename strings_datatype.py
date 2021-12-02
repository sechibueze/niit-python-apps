
firstname = 'wisdom'
lastname = 'oyibo'
fullname = firstname + ' ' + lastname
namethree = firstname * 5
size = len(firstname)
letter3 = firstname[5]

lettern = firstname[::-1]
print('Name ', lettern)

for letter in firstname:
    if letter == 's':

        # break
        continue
    print(letter)

count = 0
while count <= 10:
    print(count)
    count = count + 2