n=int(input("Enter Decimal number : "))
if (n==0):
    print(0)
else : 
    st=""
    while(n!=0):
        st=st+str(n%2)
        n=n//2
    print(f"{int(st[::-1])} in binary")