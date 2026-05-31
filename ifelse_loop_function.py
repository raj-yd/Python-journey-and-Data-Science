#To find number is odd or even
def oddeven(n):
    if n%2==0:
        return "Even"
    else :
        return "Odd"
#To find number is Positive or negative
def positivenegative(n):
    if n>=0:
        if n>0:
            return "Positive"
        else :
            return "Zero"
    else:
        return "Negative"
#To find Grade A,B,C,Fail
def grade(n):
    if n>90:
        return "A"
    elif (n<=90 and n>75):
        return "B"
    elif (n<=75 and n>60):
        return "C"
    else:
        return "Fail"
#To Print Numbers upto N
def printnum(n):
    for i in range(1,n+1,1):
        print(i)
#To Find sum of 0 to N numbers/Upto N numbers
def sumnum(n):
    sum=0
    for i in range(1,n+1,1):
        sum+=i
    return sum
#Table of Number N
def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
#To print all Prime Number between 1 to 100
def prime1to100():
    for i in range(1,101):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            print(i,end=" ")
#Factorial
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
#Fibonacci Series
def fibo(n):
    a,b=0,1
    if n==1:
        print(a)
    else :
        print(a,b,end=" ")
        for i in range(3,n+1):
            c=a+b
            print(c,end=" ")
            a=b
            b=c
#Reverse of number
def reverse(n):
    rev=0
    while (n!=0):
        d=n%10
        rev=rev*10+d
        n=n//10  # for quotient
    return rev
print("""Choose Option to find \n
1-Odd Even
2-Positive Negative
3-Grade
4-Print no. upto N Numbers
5-Sum of numbers upto N Numbers
6-Table
7-Prime no. Between 1-100
8-Factorial
9-Fibonacci Series
10-Reverse of a Number\n""")
op=int(input("Enter Option : "))
if op==1:
    n=int(input("\nEnter Number : "))
    print(oddeven(n))
elif op==2:
    n=int(input("\nEnter Number : "))
    print(positivenegative(n))
elif op==3:
    n=int(input("\nEnter Number : "))
    print(grade(n))
elif op==4:
    n=int(input("\nEnter Number : "))
    printnum(n)
elif op==5:
    n=int(input("\nEnter Number : "))
    print(sumnum(n))
elif op==6:
    n=int(input("\nEnter Number : "))
    table(n)
elif op==7:
    prime1to100()
elif op==8:
    n=int(input("\nEnter Number : "))
    print(factorial(n))
elif op==9:
    n=int(input("\nEnter nth term : "))
    fibo(n)
elif op==10:
    n=int(input("\nEnter Number : "))
    print(reverse(n))
else:
    print("Please Enter Valid Option")