for i in range(1,101):
    flag=1
    for j in range(2,i//2+1):  #for j in range(2,i):  #---method2 (less efficient)
        if i%j==0:
            flag=0
            break
    if flag==1:
        print(i)
