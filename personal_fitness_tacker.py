name=input("Enter your name : ")
weight=float(input("Enter your weight(in KG) : "))
height=float(input("Enter your height(in M) : "))
bmi=weight/(height**2)
print(f"Hey {name}")
print(f"BMI : {bmi}")
if bmi<18.5:
    print("You are Underweight....")
elif bmi>=18.5 and bmi<=24.9:
    print("You are Normalweight")
elif bmi>24.9 and bmi<=29.9:
    print("You are Overweight")
else:
    print("You are Obese") #more than 29.9
