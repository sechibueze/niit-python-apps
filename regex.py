import re

# text = 'Wisdom'
# message = ''
# print(re.match(f'Wisdom', text))
# help(re)
text = 'Wisdom'
message = 'Wisdom is  learning Python at NIIT to be wise and code'
# print(re.findall(f'^wisdom', message))
# print(re.findall(f'.de$', message))
text = 'woe'
# print(re.findall(f'(W|w)+?', message))

letters = 'r vvvvvvvvvvvvvvvvqwerty'
print(re.findall(r'^[a-zA-Z]*$', letters))
phone = '+0907867899'
print(re.findall(r'^\+?[0-9]+$', phone))
pet = 'happpy'
print(re.findall(r'hap{2}y', pet))

password = 'ada0q@wert' # {8, 12}
# print(re.findall(f'[A-Za-z0-9@]*', password))
# [A-Z-a-z]
# [0-9]
# [A-Za-z0-9@]*

# Email

# wisdom2309@gmai.com
email = 'wiWsdo-m2309gm5ai.ai'
email_pattern = r'[A-Za-z0-9\-_\.]+@[a-zA-Z0-9]+\.[A-Za-z]{2,3}'
print(re.findall(email_pattern, email))