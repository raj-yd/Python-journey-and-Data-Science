class Students:
    # constructor, can be called implicitly
    # python constructor is used to create the data members (variables/properties) of the class
    # and also to initialize 
    # self: key variable holds reference of the object which is being created (current obj)
    # self is a mandatory argument must be given to every class' constructor
    def __init__(self,name,rollno,marks,city):
        self.name=name
        self.rollno=rollno
        self.marks=marks
        self.city=city
        print("New Students Register Successfully")
        print(f'self = {self}')

# object of Student class
# we are passing all the required details (property' values)
stu1=Students("Raj",42,89,"Prayagraj")
print(f"stu1.name = {stu1.name}")
print(stu1)
stu2=Students("Harsh",38,88,"Amethi")
print(f"stu2.name = {stu2.name}")
print(stu2)