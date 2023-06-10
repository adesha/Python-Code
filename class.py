class dog:
    att1='Mammal'
    att2='Dog'

    def func(self):
        print(self.att1)
        print(self.att2)



Tony=dog()
Tony.func()

class Person:

    def __init__(self,name):
        self.name=name

    def intro(self):
        print(self.name)


p=Person('Rahul')
p.intro()