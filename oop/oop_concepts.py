

# class Animal:
#     name = 'Animal'
#     def move(self):
#         print('{} is moving'.format(self.name))
#     def eat(self):
#         print('{} is eating'.format(self.name))
#     def sleep(self):
#         print('Animal is sleeping')
#     def cry(self):
#         print('{} is crying'.format(self.name))
#
# class Dog(Animal):
#     name = 'Dog'
#
#     def move(self):
#         print('{} is runinning'.format(self.name))
#
# animal1 = Animal()
# # animal1.name = ''
# animal1.move()
# animal1.sleep()
# dog1 = Dog()
# dog1.move()
# dog1.cry()


# -------- Encapsulation ----------
class Animal:
    __name = 'Animal'
    def move(self):
        print('{} is moving'.format(self.__name))
    def __eat(self):
        print('{} is eating'.format(self.__name))
    def __sleep(self):
        print('{} is sleeping'.format(self.__name))
    def __cry(self):
        print('{} is crying'.format(self.__name))

# class Dog(Animal):
#     name = 'Dog'
#
#     def move(self):
#         print('{} is runinning'.format(self._name))
#     def say_move(self):
#         pass

animal1 = Animal()
animal1.move()
# animal1.name = 'Whiller'
# animal1.move()
# animal1.sleep()
# dog1 = Dog()
# dog1.move()
# dog1.cry()