list1=[1,2,3,4]
#what happens when you do the following 
list2=list1
print(list2)
# the reference which is holded by list1, now list2 is also pointing to the same reference.
#Single Reference, and multiple pointers

print('after copying reference: ')
print(f"id(list1) = {id(list1)}")
print(f"id(list2) = {id(list2)}")

print('Before appending: ')
print(f"list1 = {list1}")
print(f"list2 = {list2}")

list1.append([10,20])
print(f"list1 = {list1}")
print(f"list2 = {list2}")

#the first approach: .copy()
list2=list1.copy()  #creates a new list, and this is called shallow copy method

print("After .copy() and .append()")
list1.append([30,40])
print(f"list1 = {list1}")
print(f"list2 = {list2}")

print(f"id(list1) : {id(list1)}")
print(f"id(list2) : {id(list2)}")

#another shallow copy method using slicing
list2=list1[:]

#shallow copy me list ke andar jo elements hai "nested list",etc uska refrence same hi rahega bahar wale list ka refrence diffrent hoga
print(f"id(list1[4]) : {id(list1[4])}")
print(f"id(list2[4]) : {id(list2[4])}")

#constructor copying
list3=list(list1)
#list is the name of object which is used here for the creation of new memory (object) having the same values as in list1 by passing in the constructor (the function which is called implicitly)


#Deep copy apprach (different than shallow copy)
list4=[1,2,3,[4,5]]  #nested list
# list4 <- 1,2,reference -> [3,4]
list5 = list4.copy() #shallow
list4.append([10,20])
print(f"list4 = {list4}")
print(f"list5 = {list5}")

list4[3][0]=6  #modified inner list of list4
print("list4[3][0]=6")
print(f"list4 = {list4}")
print(f"list5 = {list5}")

#The Solution: use .deepcopy() through copy object, this object must be imported before using it.
import copy
list6=copy.deepcopy(list4)
list4[3][0]=9
print('after using .deepcopy()')
print("list4[3][0]=9")
print(f"list4 = {list4}")
print(f"list6 = {list6}")