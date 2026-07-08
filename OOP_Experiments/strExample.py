class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

stu1=Student("Aman",86)
stu2=Student("Raman",87)

print(f"stu1 = {stu1}")
print(f"stu2 = {stu2}")

########################################################################
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __str__(self):     #__str__ modifies the default object string
        return f"Student {self.name} , Marks {self.marks}"

stu1=Student("Aman",86)
stu2=Student("Raman",87)

print(f"stu1 = {stu1}")
print(f"stu2 = {stu2}")