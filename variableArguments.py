#Variable Arguments - unknown number of inputs in function
#*args collects all extra positional arguments into a TUPLE.

#The name args is jist a conventional name. 

# * is important here

def add_all(*numbers):
    #print(type(numbers))
    #here numbers is a Tuple
    total=0
    for curr in numbers:
        total+=curr
    return total
     
print(f"add_all(1,2,3,4) = {add_all(1,2,3,4)}")
print(f"add_all(101,62,3,724,2,272) = {add_all(101,62,3,724,2,272) }")

#Another concept: Key Variable Arguments

#*kwargs

# collects information into DICTIONARY

def print_details(**details):
    for key , value in details.items():
        print(f"{key} : {value}")
print_details(name='Raj',age=20,std=12,location='Prayagraj')
