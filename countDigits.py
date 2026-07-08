num=int(input("Enter number : "))
# print(f"{len(str(num))} digits") #method 1

# method 2
count=0
while(num!=0):
    count+=1
    num=num//10
print(f"{count} digits")