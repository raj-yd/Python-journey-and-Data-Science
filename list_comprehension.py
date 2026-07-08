# my_list=int(input("Enter number separeted by space : ").split())   --------- error dega

# List comprehension
# [expression for item in iteratble if condition]
# expression: value to be stored
# item: variable representing each element in the iterable
# iterable: sequence like list,tuple,range,etc
# condition(optional): filters which items to include

my_list=[int(i) for i in input("Enter number separeted by space : ").split()] # condition nhi lagaya hu jarurat nhi thi
print(my_list)