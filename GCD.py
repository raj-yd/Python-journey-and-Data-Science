num1=int(input("Enter first number : "))
num2=int(input("Enter Second Number : "))
n=num1 if (num1<num2) else num2
gcd=1
for i in range(2,n+1) :
    if (num1%i==0 and num2%i==0):
        gcd=i
print("Greatest Common Divisor(GCD) : ",gcd)