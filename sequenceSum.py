# take n input from the user 
# sum the elements in sequence
# sequence : 1:n
# print sum
# validate the input also
# input >=1
# our desired output is 
# sum of sequence 0+1+2+3+4.....+n=sum
n=int(input("Enter the number : "))
sum=0
if n>=1:
    print("Sum of Sequence ",end="")
    for i in range(1,n+1):
        print(f"{i}",end="+" if i!=n else "=")  # ternary operator used
        sum+=i
    print(f"{sum}")
else:
    print("Please enter valid number")

