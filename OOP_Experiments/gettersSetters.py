class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    
    #Getter  #In java, getName()
    #controlled reading access
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks
    
    #Setter - controlled writing access with validation
    def set_marks(self,marks):
        if 0<marks<=100:
            self.__marks=marks
            print(f'Marks updated to {marks}')

    def set_name(self,name):
        if len(name.strip())>0:
            self.__name=name
        else:
            print('Name cannot be empty')

student1=Student("Raj",85)
print(student1.get_name())
print(student1.get_marks())
student1.set_marks(90)
print(student1.get_marks())

student1.set_marks(95) #valid
student1.set_marks(150) #invalid
student1.set_marks(-10) #invalid