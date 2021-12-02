from Question import Question
from data import questionBank
from Paper import Paper


# print(Question)
paper_questions = []
for q in questionBank:
    # print(q)
    text = q['text']
    choices = q['options']
    correct_answer = q['correct_answer']
    question = Question(text, choices, correct_answer)
    paper_questions.append(question)

paper1 = Paper('Python', paper_questions)
paper1.start_paper()