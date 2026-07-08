num=int(input("Enter number : "))
flag=1
for i in range(2,num//2+1):
    if num%i==0:
        flag = 0
        break
if flag==1:
    print(f"{num} is a prime number ")
else :
    print(f"{num} is not a prime number")