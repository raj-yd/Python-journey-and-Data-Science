# Syntax
# [on true] if [expression] else [on false]
age=int(input("Enter Age : "))
status="Eligible for voting" if (age>=18) else "Not eligible for voting"
print(f"You are {status}")