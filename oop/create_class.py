
# class Dog:
#     name = ''
#     position = 0

# suzzy = Dog()
# suzzy.name = 'Suzzy'
# suzzy.position = 25
# print(suzzy.name)
# print(suzzy.position)

class Dog:
    name = ''
    position = 0
    energy_level = 'low'

    def __init__(self, name, pos):
        self.name = name
        self.position = pos
    def get_energy_level(self):
        return  self.energy_level
    def set_energy_level(self, level):
         self.energy_level = level
    def run(self):
        level = self.get_energy_level()
        if(level == 'low'):
            self.position = self.position + 5
        elif(level == 'medium'):
            self.position = self.position + 50
        elif (level == 'high'):
            self.position = self.position + 150



dutty = Dog('Dutty', 15)
print(dutty.position)
print(dutty.name)
dutty.run()
dutty.set_energy_level('high')
dutty.run()
print(dutty.position)