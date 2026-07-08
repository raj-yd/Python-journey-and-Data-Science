num1=int(input("Enter first number : "))
operator=input("Enter Operator(+,-,*,/) : ")
num2=int(input("Enter second number : "))
if operator=="+":
    print(f"{num1}+{num2}={num1+num2}") #Addition
elif operator=="-":
    print(f"{num1}-{num2}={num1-num2}") #Subtraction
elif operator=="*":
    print(f"{num1}*{num2}={num1*num2}") #Multipication
elif operator=="/":
    print(f"{num1}/{num2}={num1/num2}") #division->Quotient
else:
    print("Please Enter Operator + or - or * or /")