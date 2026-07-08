#list creating using same type -- homgeneous
fruits=["apple","banana","mango","orange"]

#list creating using mixed type -- hetrogeneous
student=["Raj",20,8.5,True]

print(f"fruits = {fruits}")
print(f"type(fruits) = {type(fruits)}")
print(f"student = {student}")
print(f"trpe(student) = {type(student)}")

#list is a bilt-in data type used to store an oredered, mutable collection of items in a single variable
#list are created by commas and enclosed in []

#empty list
empty=[]

#list creation using list() constructor:called implicity (apne app call ho jaye)

another_fruits=list(fruits)
print("another_fruits",another_fruits)  #['apple', 'banana', 'mango', 'orange']
number_list=list([1,2,3,4,5])

# print(list(1,2,3,5))  this will give an error
#list creating using tuple
number_list=list((10,20,30,40,50))

#repeated element in list
zeros=[0]*5
print(f"Zeros - {zeros}") #[0, 0, 0, 0, 0]
my_list=[["Fruits"]*3,45,5]
print(f"my_list - {my_list}") #[['Fruits', 'Fruits', 'Fruits'], 45, 5]

#accessing elements in list
print(f"fruits[0]-{fruits[0]}")
print(f"number_list[2]-{number_list[2]}")

# negative indexing
print(f"fruits[-2]-{fruits[-2]}")  #last second

#slicing
print(f"fruits[0:3]-{fruits[0:3]}")
print(f"number_list[1:3]-{number_list[1:3]}")

#list is a mutable
print(f"fruits={fruits}")
fruits[1]="pineapple"
print(f"fruits={fruits}")  #banana is replaced by pineapple because list is a mutable datatype

int_values=[x for x in range(10,101,10)]
print(f"int_values={int_values}")  #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#some more slicing
print(f"int_values[:3]={int_values[:3]}")
print(f"int_values[6:]={int_values[6:]}")
print(f"int_values[::2]={int_values[::2]}")
print(f"int_values[::-1]={int_values[::-1]}") #[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]   ------- reverse
print(f"int_values={int_values}")

num=[55,12,13,12,55,99,12,14,20,12,99]
print(f"num={num}")
#first 3 numbers
print(f"first 3 numbers = {num[:3]}")
#last 3 numbers
print(f"last 3 numbers = {num[-3:]}")
#mid number
print(f"middle number = {num[len(num)//2]}")
#summing
print(f"Sum={sum(num)}")
#average
print(f"average={sum(num)/len(num)}")
#repeated values [55,12,13,12,55,99,12,14,20,12,99]
for i in num:
    pass

words = ["United","Prayagraj","Raj","Naini"]
#finding largest size element carried
max1=0
largest_element=""
for i in words:
    if max1<len(i):
        max1=len(i)
        largest_element=i
print(f"maximun size element contains {max1} characters and it is {largest_element}")

#method2 for finding largest words
print(max(words,key=len)) #Prayagraj

#finding all strings tied for maximum length
words = ['orange', 'banana', 'kiwi', 'cherry']
print('max(words)', max(words))  #orange

max_len=max([len(word) for word in words])
print(f"[len(word) for word in words] = {[len(word) for word in words]}") #[len(word) for word in words] = [6, 6, 4, 6]
print(f"max_len={max_len}")  #max_len=6

max_len = max(len(word) for word in words)  #Generator does not store [6, 6, 4, 6] It produces: 6 → 6 → 4 → 6(one by one)  #Compares → max = 6
print(f"(len(word) for word in words) = {(len(word) for word in words)}")  #(len(word) for word in words) = <generator object <genexpr> at 0x000002054F2F18C0>
print('max_len', max_len)  #max_len 6
#iterating over words, word by word, and checking if the current word length matches with max_len (that is previously calculated using max()), then append that word in the list
all_largest=[ word for word in words if len(word)==max_len]
print("All largest",all_largest)

#Adding elements into the list
print(f"words = {words}")
#using append
words.append("grapes")
print(f"words = {words}")
#using insert
words.insert(1,"apple")
print(f"words = {words}")
#using extend
words.extend(["pineapple","watermelon"])
print(f"words = {words}")