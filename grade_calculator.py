

score = 0
grade = 'R'

if(score >= 70):
    grade = 'A'
elif(score >= 60 and score < 70):
    grade = 'B'
elif(score >= 50 and score < 60):
    grade = 'C'
elif(score >= 40 and score < 50):
    grade = 'D'

def get_grade(score):
    grade = ''
    # print(grade, 'from function')
    if (score >= 70):
        grade = 'A'
    elif (score >= 60 and score < 70):
        grade = 'B'
    elif (score >= 50 and score < 60):
        grade = 'C'
    elif (score >= 40 and score < 50):
        grade = 'D'
    else:
        grade = 'F'
    return  grade

my_grade = get_grade(89)
ade = get_grade(80)
sam = get_grade(45)
print(my_grade, ade, sam)

print(2 ** 4)
print(16 ** .5)

print(type(2.0))