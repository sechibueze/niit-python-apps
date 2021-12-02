
class Course:
    id = ''
    weight = 0
    score = 0
    grade_point = 0

    def __init__(self, id, weight, score):
        self.id = id
        self.weight = weight
        self.score = score
    def set_grade_point(self):
        self.grade_point = self.calculate_grade_point()
    def get_course_rating(self):
        self.set_grade_point()
        return self.weight * self.grade_point
    def calculate_grade_point(self):
        grade = self.calculate_grade()
        if grade == 'A':
            return 5
        elif grade == 'B':
            return 4
        else:
            return 0

    def calculate_grade(self):
        if self.score >= 70:
            return 'A'
        elif self.score > 60 and self.score <70:
            return 'B'
        else:
            return 'F'

c1 = Course('web', 3, 66)
print(c1.get_course_rating())