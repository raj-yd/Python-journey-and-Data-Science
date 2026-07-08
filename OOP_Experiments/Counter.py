class Student:
    count=0 # class variable

    #constructor
    def __init__(self,name):
        self.name=name
        Student.count+=1
        print(f"Student #{Student.count} : {self.name} Registered")

Student("Aman")
Student("Raman")