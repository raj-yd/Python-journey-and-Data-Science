def addnumbers(num1 , num2):
    result = num1+num2
    return result
#Take a validator to check whether is this a positive number then process with add_numbers()
#Use while to take inputs
#Stop when you get negative
while True:
    num1=int(input("Enter number 1 : "))
    num2=int(input("Enter number 2 : "))
    if (num1>=0 and num2>=0):
        result=addnumbers(num1 , num2)
        print(f"Addition of {num1} and {num2} is {result}")
    else :
        print("You have entered a negative number ... exiting....")
        break