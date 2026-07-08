print(range(10)) # range(0, 10)
print(type(range(10))) # <class 'range'>
list_of_elements=range(10)
print(type(list_of_elements)) # <class 'range'>
print(list_of_elements) # range(0, 10)
print("\n")
for i in range(5): 
    print(f"{i}")
# output 0
#        1
#        2
#        3
#        4
print("\n")
for i in range(10,21): # 10 to 20
    print(f"{i}",end=" ")
print("\n")
for i in range(10,21,2): # 10 12 14 16 18 20
    print(f"{i}",end=" ")
print("\n")
for i in range(5,0): # no output
    print(f"{i}",end=" ")
print("\n")
for i in range(5,0,-1): # 5 4 3 2 1
    print(f"{i}",end=" ")