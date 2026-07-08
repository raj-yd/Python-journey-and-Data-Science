class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def describe(self):
        print(f"Hi i am {self.name} , and my age {self.age}")

class Dog(Animal):
    def __init__(self, name , age ,breed):
        super().__init__(name,age)
        self.breed=breed
    def describe(self):
        super().describe()
        print(f"Breed : {self.breed}")

dog=Dog("Rocky",5,"German")
dog.describe()