#define a function that accepts a list having number of elements, and return max and min from the function
#in function calling statement, accept those two max and min values through tuple packing mechanism
#also perform unpacking mechanism to take those values (max and min) in individual variables

def findingMinMax(nums):
    return max(nums),min(nums)

minMax=findingMinMax([int(x) for x in input("Enter numbers separeted by space : ").split()])  #packing
minimum,maximum=minMax # unpacking
print(f"Minimun = {minimum}\nMaximum = {maximum}")
