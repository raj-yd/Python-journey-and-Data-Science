def greet(name):  #formal argument
    print(f'Hello, {name} ')

print("Enter exit for Exit ")

while True:
    name=input("Enter Name : ")
    if (name=="exit" or name=="Exit"):
        break
    greet(name) #actual argument
