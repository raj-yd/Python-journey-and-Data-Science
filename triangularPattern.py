"""
Output- 

*
**
***
****
*****

"""

rows=int(input("Enter number of rows : "))
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()

#method 2
rows=int(input("Enter number of rows : "))
for i in range(1,rows+1):
    print("* "*i)