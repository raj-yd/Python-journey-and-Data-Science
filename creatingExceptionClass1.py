class EligibilityError(Exception):
    pass

def check_eligibility(age):
    if age < 0:
        raise EligibilityError("Age cannot be Negative ")
    if age>150:
        raise EligibilityError("Age cannot be greater than 150 ")
    return f"Your age is {age} and you are eligible "

try:
    age=int(input("Enter age : "))
    print(f"{check_eligibility(age)}")
except EligibilityError as e:
    print(f"{e}")
else :
    print("Everything Run Successfully")