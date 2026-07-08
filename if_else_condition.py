#if condition
age=int(input("Enter your age : "))
if (age>=18):
    print("You are eligible for Voting")

#if else condition
age=int(input("Enter your age : "))
if (age>=18):
    print("You are eligible for Voting")
else :
    print("You are not eligible fot Voting")

#multiple condition if, elif, else
age=int(input("Enter your age : "))
if ( age>=1 and age<=12):
    print("Child")
elif(age>12 and age<= 18):
    print("Teenage")
elif(age>18 and age<=40):
    print("Adult")
else:
    print("Senior Citizen")