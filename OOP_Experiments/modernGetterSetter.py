class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    
    #modern way: using annotation /decorator
    @property
    def name(self):
        return self.__name  #getter
    @property
    def marks(self):   #getter
        return self.__marks
    
    @marks.setter #works like a stter
    def marks(self,marks):
        if 0<marks<=100:
            self.__marks=marks
            print(f'Marks updated to {marks}')
    @name.setter
    def name(self,name):
        if len(name.strip())>0:
            self.__name=name
        else:
            print('Name cannot be empty')

student1=Student("Raj",85)
print(student1.name)
print(student1.marks)

student1.name="Aniket"
student1.marks = -500 #invalid
student1.marks = 260 #invalid
student1.marks = 71 #valid

print(student1.name)
print(student1.marks)