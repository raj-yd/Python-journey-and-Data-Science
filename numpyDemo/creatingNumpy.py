import numpy as np

#numpy creating using list
arr1=np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))   #<class 'numpy.ndarray'>
print(arr1.dtype)    #datatype  (numpy) ---->int64

arr2=np.array([1.45,12.5,45.78,432.09,215.34])
print(arr2)
print(type(arr2))  #<class 'numpy.ndarray'>
print(arr2.dtype)  #float64

#2D array (matrix)
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(f"Shape of {matrix} : {matrix.shape}")
print(f"Dimension of {matrix} : {matrix.ndim}")