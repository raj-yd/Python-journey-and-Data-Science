#take input in number from the user continuously until user for infinite times but if you recieve negative ValueError break the loop
#for positive - print the same
#for negative - break the loop
i=1
while (i==1):
    n=int(input("Enter number : "))
    if (n<0):
        i=0
        print("Thankyou")
    else:
        print(f"You Entered number {n}")

# method 2 using break statement
# while (True):
#     n=int(input("Enter number : "))
#     if (n<0):
#         print("Thankyou")
#         break
#     else:
#         print(f"You Entered number {n}")