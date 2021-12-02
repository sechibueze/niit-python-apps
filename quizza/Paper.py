
class Paper:
    title = ''
    questions = []
    score = 0

    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
    def start_paper(self):
        for ii, Question in enumerate(self.questions):
            is_correct_answer = Question.show_question()
            if is_correct_answer:
                self.score += 1
            if ii == len(self.questions) - 1:
                self.show_result()
    def show_result(self):
        print('Quiz ended')
        message = 'Your score in {} is {}/{}'.format(self.title, self.score,len(self.questions))
        print(message)



