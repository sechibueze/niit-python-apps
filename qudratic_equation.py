# This script calculates the solution of a qudartic equation
# of the form: ax^2 + bx + c = 0

# Accept input from users
print("-----QudraticSolverApp-----")
print('Solve the quadratic equation: ax^2 + bx + c = 0')
a = int(input("Enter your a value : "))
b = int(input("Enter your b value : "))
c = int(input("Enter your c value : "))

# Calculate descriminant
root_type = ''
descri = b**2 - 4 * a * c
descri_root = descri ** .5
x1 = (-1 * b + descri_root) / 2 * a
x2 = (-1 * b - descri_root) / 2 * a

if descri == 0:
    root_type = 'Double roots'
elif descri < 0 :
    root_type = 'Complex root'
else:
    root_type = 'Real root'

# Display results
print("Type of roots : ", root_type)
print("The solution is: ", (x1, x2))


