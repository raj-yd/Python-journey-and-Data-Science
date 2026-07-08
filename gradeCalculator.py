percent=int(input("Enter Percentage : "))
if (percent <= 100 and percent>=90):
    print("Grade A")
elif (percent <= 89 and percent>=75):
    print("Grade B")
elif (percent <= 74 and percent>=60):
    print("Grade C")
elif (percent <= 59 and percent>=40):
    print("Grade D")
elif (percent <= 39 and percent>=0):
    print("Grade F")
else :
    print("Please Enter Valid Percentage")