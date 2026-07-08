# finding largest among the sequence using for loop
# sequence : input().split()
my_list=input("Enter number separeted by space : ").split()
max=int(my_list[0])
for i in my_list:
    if (int(i)>max):
        max=int(i)
print(f"Maximum number = {max}")

# method 2
my_list=[int(i) for i in input("Enter number separeted by space : ").split()] #using list comprehension
max=my_list[0]
for i in my_list:
    if (i>max):
        max=i
print(f"Maximum number = {max}")
