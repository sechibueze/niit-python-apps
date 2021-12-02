# This program calculates the factrial of a number n

# print(range(2, 10, 2))

def find_factorial(n):
    factorial = 1
    for step in range(1, n + 1):
        factorial = step * factorial
    return factorial
n = int(input('Enter your integer : '))

print(find_factorial(n))