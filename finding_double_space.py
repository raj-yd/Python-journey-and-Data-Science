#Method 1
st=input("Enter String : ")
for i in range(len(st)-1):
    if st[i]==" " and st[i+1]==" ":
        print("Double Space found at index ",i)
# Method 2
index=st.find("  ")
if index==-1:
    print("Not found")
else :
    print("Found at index ",index)