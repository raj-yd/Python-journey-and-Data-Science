#Observe the following functions:
# 1. tupleObj.count(value)
# 2. tupleObj.index(value)
# 3. len(tupleObj)
# 4. sum(tupleObj)
# 5. max(tupleObj)
# 6. min(tupleObj)
# 7. And, try to modify the tuple with the help of list
tupleSample = (78, 98, 36, 59, 78, 24, 78)
print(f"tupleSample = {tupleSample}")
print(f"tupleSample.count(78) = {tupleSample.count(78)}")
print(f"tupleSample.index(36) = {tupleSample.index(36)}")
print(f"len(tupleSample) = {len(tupleSample)}")
print(f"sum(tupleSample) = {sum(tupleSample)}")
print(f"max(tupleSample) = {max(tupleSample)}")
print(f"min(tupleSample) = {min(tupleSample)}")

#transformation and modification
mylist=list(tupleSample)
mylist[-1]=40
newTuple=tuple(mylist)
print('modified tuple using list: ', newTuple)