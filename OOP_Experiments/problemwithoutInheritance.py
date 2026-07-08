#Problem Without inheritance
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    def bark(self):
        print(f"{self.name} says : Woof! Woof!")


class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    def meow(self):
        print(f"{self.name} says : Meow! Meow!")
