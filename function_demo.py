
# Define a function
def check_even_number(number_to_check = 3, message = ''):
    print(message)
    is_even = number_to_check % 2 == 0

    if(is_even):
        print(number_to_check, 'is an even number ',)
    else:
        print(number_to_check, 'is an odd  number ',)

# check_even_number(310009, 'This function cheks if a number is even or not')

# check_even_number(310009)
# check_even_number()
def get_total(x, y):
    sum = x + y
    return sum
    # print('Hi')

total = get_total(394, 43)
if(total > 100):
    print('Too costly')
else:
    print('OK')
# print(total)