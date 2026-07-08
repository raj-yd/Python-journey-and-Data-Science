import numpy as np
matrix=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(matrix)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

print(matrix[0,0])  #row 0, col 0 => 10
print(matrix[1,2])  #row 1, col 2 => 60

#entire array row printing
print(matrix[0])

#entire array column printing
print(matrix[:,0])  #first column [10, 40, 70]
print(matrix[:,1])   #second column

#sublist or subarray
print(matrix[0:2, 1:3]) #top-right 2x2 portion)