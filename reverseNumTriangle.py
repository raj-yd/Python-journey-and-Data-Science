rows=int(input("Enter number of rows : "))
for i in range(1,rows+1):
    for j in range(rows,i-1,-1):
        print(j,end=" ")
    print()

# output-
# Enter number of rows : 5
# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3 
# 5 4 
# 5 