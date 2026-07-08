#problem without super()
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#Option 1:
class Dog(Animal):
    def __init__(self, name, age,breed):
        #without super()
        self.name=name  #Repeatation
        self.age=age  #Repeatation
        self.breed=breed  #Repeatation

#Solution: super()
class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name,age)
        self.breed=breed
        print(f'Dog breed set: {self.breed}')


    def describe(self):
        #Animal
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        #Dog
        print(f"Breed : {self.breed}")

#Note: comment one Dog definition to test it, create number of objects and test by passing different values

dog1=Dog("Tommy",2,"German")
dog1.describe()