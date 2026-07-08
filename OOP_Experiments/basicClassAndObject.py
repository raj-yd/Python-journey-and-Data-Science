#class definition in python
class Student:
    pass
#creating object from class
obj1=Student()
obj2=Student()
#another example : list([1,2,3])
print(type(obj1))
print(obj1)

obj1.name="Raj"
obj1.age=20

obj2.name="Akshat"
obj2.age=19

print(f"obj1.name = {obj1.name}")
print(f"obj2.name = {obj2.name}")

#what if, you create an object, and during the object creation, you could pass the initial values to the properties declared by the class associated with
# int x;
# x = 10;
# int y = 20;
#This operation can be done through the special function inside the class, called "Constructor". It called implicitly (automatically), when you create an object.
#next file: constructorInClass.py