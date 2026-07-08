class Animal:
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print(f"{self.name} is speaking ")

    def move(self):
        print(f"{self.name} is Moving ")

class Dog(Animal):
    #repeat method in child class
    #speak() is overridden
    #it overrides the method speak() in superclass
    def speak(self):
        print(f"{self.name} Speaks woof! woof! ")

class Cat(Animal):
    #repeat method in child class
    #overridden methods
    def speak(self):
        print(f'{self.name}: meow! meow!')
    
    def move(self):
        print(f'{self.name} sneaks silently')

class Fish(Animal):
    pass
print(Animal.__subclasses__())
dog=Dog("Ronny") 
dog.speak()#its own method
dog.move()#call to super class method
cat=Cat("Mimmi")
cat.speak()#call to Cat' method
cat.move()#call to Cat' method
fish=Fish("Whale")
fish.speak()#call to super class method
fish.move()#because it is not overridden 