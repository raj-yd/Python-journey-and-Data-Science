class Employee:
    def __init__(self,name,salary,post,gender): #constructor
        self.name=name
        self.salary=salary
        self.post=post
        self.gender=gender
        print("Employee Registered Successfully")
    def Display(self,workhour): #function
        print(self.name)
        print(workhour)
    def Display2(self,salary): #function
        print(self.salary)
        print(salary)
        # print(workhour)  #this will give error because it is not defined in constructor
obj1=Employee("Priyanshu",180000,"CEO","Male")
obj2=Employee("Raj",280000,"Founder","Male")
# print(obj1.name)
# print(obj2.name)
obj1.Display(12)
obj1.Display2(100000)