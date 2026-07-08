import numpy

numarray=numpy.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

#indexing and slicing
# method 1 - casual Approach
# print(numarray[1])
# print(numarray[-1])
# print(numarray[0:2])
# print(numarray[0:2][1])
# print(numarray[0:2][1][1])

# method 2

print(numarray[:,])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# print(numarray[,:])  #---> error--->invalid syntax
print(numarray[:,:])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(numarray[2,2])  #2
print(numarray[1:3,1:3])
# [[5 6]
#  [8 9]]
print(numarray[1:3,1:2])
# [[5]
#  [8]]