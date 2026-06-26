class Animal:
    def __init__(self, color, name):

        self.color = color
        self.name = name

    def make_sound(self):


        print("I'm an animal")


class Dog(Animal):
    def __init__(self, color, name, master):
        Animal.__init__(self, color, name)
        self.master = master
        
    def make_sound(self):
        print('bark')