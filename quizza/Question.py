
class Question:
    question_text = ''
    options = []
    correct_answer = ''

    def __init__(self, text, options, ca):
        self.question_text = text
        self.options = options
        self.correct_answer = ca

    def show_question(self):
        print(self.question_text)
        for index, opt in enumerate(self.options):
            print('({}) : {}'.format(index, opt))
        return self.get_attempt()
    def get_attempt(self):
        attempt = input("Type your answer : ")
        return self.check_attempt(attempt)

    def check_attempt(self, attempt):
        selected_attempt = self.options[int(attempt)]


        if self.correct_answer == str(selected_attempt):

            return True
        return False


