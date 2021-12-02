from Course import Course
from utils import calculate_total
import math

courses = [
    {
        "id": "WCD101",
        "weight": 4,
        "score": 66
    },
   {
        "id": "SE101",
        "weight": 5,
        "score": 76
    },
]

course_ratings = []
course_weights = []
for course_item in courses:
    id = course_item.get('id')
    weight = course_item.get('weight', 0)
    score = course_item.get('score', 0)
    course = Course(id, weight, score)
    course_ratings.append(course.get_course_rating())
    course_weights.append(weight)


cgp = calculate_total(course_ratings) / calculate_total(course_weights)
print(cgp)