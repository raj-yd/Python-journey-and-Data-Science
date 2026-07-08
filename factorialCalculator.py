n=int(input("Enter Number : "))
factorial=1
for i in range(n,0,-1):
    factorial*=i
print(f"Factorial = {factorial}")