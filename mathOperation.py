pi=3.14
def addition(*numbers):  #typr of *numbers is tuple
    add=0
    for i in numbers:
        add+=i
    return add
def subtraction(a,b):
    return a-b
def multiply(*numbers):
    mul=1
    for i in numbers:
        mul*=i
    return mul
def floor_division(val1,val2):
    return val1//val2