#Solution: Generalization using inheritance
#Generalization: Relations in between parent and child
#Aquiring the traits (features/behavior/property) from parent in child
#Avoid writing the common definition for all the specific classes

#Parent Class / Super Class /Base
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def __str__(self):
        return f"I am {self.name}, my age is {self.age}"

#child class 1 / subclass / derived
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says : Woof! Woof!")
class Cat(Animal):
    def meow(self):
        print(f"{self.name} says : Meow! Meow!")
class Parrot(Animal):
    def talk(self,message):
        print(f'{self.name}, message: {message}')

dog=Dog("Gullu",4)
cat=Cat("Gulli",3)
parrot=Parrot("Tom",1)
print(dog)
dog.eat()
dog.bark()
print(cat)
cat.eat()
cat.meow()
print(parrot)
parrot.eat()
parrot.talk("Hello Gullu your gulli is calling you...hahahaahaha")