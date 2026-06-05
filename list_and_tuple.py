#Program to store seven fruits in a list entered by the user.
fruits=[]
for i in range(7):
    print("Enter Fruit ",i+1," : ");
    f=input()
    fruits.append(f)
print("Your Fruits is ",fruits)

#Write a program to accept marks of 6 students and display them in a sorted manner.
marks=[]
print("Enter Marks of 6 Students")
for i in range(0,6,1):
    m=int(input())
    marks.append(m)
marks.sort()
print("Marks in sorted manner : ",marks)

 #Check that a tuple type cannot be changed in python.
try:
    tuple=(1,3,5,2,4)
    tuple[2]=40
    print(tuple)
except:
    print("Tuple cannot changed because it is an immutable")
    
#Write a program to sum a list with 4 numbers.
num=[]
print("Enter 4-Numbers")
for i in range(4):
    n=int(input("Enter Number here : "))
    num.append(n)
sum=sum(num)
print("Sum of all 4 numbers is ",sum)

#Write a program to count the number of zeros in the following tuple
tup=(3,2,"Okay",4,6,0,1,5,0,7)
c=tup.count(0)
print("Number of zeros in tuple ",tup," is ",c)