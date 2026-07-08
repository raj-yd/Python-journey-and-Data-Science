class Animal:
    def __init__(self,name):
        self.name=name

    def speaks(self):
        pass

class Dog(Animal):
    #overridden
    def speaks(self):
        print(f"{self.name} says Woof! Woof!")

class Cat(Animal):
    def speaks(self):
        print(f"{self.name} says Meow! Meow!")

class Cow(Animal):
    def speaks(self):
        print(f"{self.name} says moo! moo!")

class Duck(Animal):
    def speaks(self):
        print(f"{self.name} says quack! quack!")

#myobj=ClassNAme()
animals=[Dog("Rocky"),Cat("Gulli"),Cow("Lulu"),Duck("Ferry")]
for i in animals:
    i.speaks()