import numpy as np

#array of zeros
zeros=np.zeros(10)
print(zeros)

#array of ones
ones = np.ones((3,3))  #3x3 matrix of ones
print(ones)

#providing range
arr=np.arange(1,11) #1-10
print(arr)

arr=np.arange(0,1.1,0.1) #with float steps
print(arr)

arr=np.linspace(0,1,5)
print(arr)

rand_int=np.random.randint(1,100,10)
print(rand_int)

rand_float=np.random.random(5)  #0-1 ,1is excluded
print(rand_float)