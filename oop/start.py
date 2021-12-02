
class Animal:
    name = ''
    location = 0

    def __init__(self, name, location = 0):
        self.name = name
        self.location = location
    def run(self):
        self.location = self.location + 50
    def show(self):
        message = '{} is at {}'.format(self.name, self.location)
        print(message)


bingo = Animal('Bingo')
fluffy = Animal('Fluffy', 80)
fluffy.location = 200
bingo.run()
bingo.run()
fluffy.run()
bingo.show()
fluffy.show()