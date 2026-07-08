"""
Output- 

*****
*****
*****
*****
*****

"""

rows=int(input("Enter number of rows : "))
for i in range(rows):
    for j in range(rows):
        print("*",end=" ")
    print()

#method 2
rows=int(input("Enter number of rows : "))
for i in range(rows):
    print("* "*rows)