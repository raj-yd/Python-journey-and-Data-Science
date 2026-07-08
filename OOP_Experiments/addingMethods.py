#Student class definition
class Student:
    #constructor
    def __init__(self,name,marks,age):
        self.name=name
        self.age=age
        self.marks=marks
    #methods
    def introduce(self):
        print(f"Hi I am {self.name}, {self.age} years old")
    
    def get_grade(self):
        if self.marks>=90: return "Grade A+"
        elif self.marks>=80: return "Grade A"
        elif self.marks>=70: return "Grade B"
        elif self.marks>=40: return "Grade C"
        else : return "Fail"

    def is_passed(self):
        return self.marks>=40
    
    def report_card(self):
        print('='*30)
        print("    STUDENT REPORT CARD  ")
        print('='*30)
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Marks : {self.marks}")
        print(f"Result : {'PASS' if self.is_passed() else 'FAIL'}")
        print('='*30)


stu1=Student("Raj",85,20)
stu2=Student("Priyanshu",78,19)
stu3=Student("Deepak",32,19)

stu1.introduce()
stu1.report_card()

stu2.introduce()
stu2.report_card()

stu3.introduce()
stu3.report_card()