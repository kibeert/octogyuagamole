import numpy as np
print(np.__version__)
arr = np.array([1,2,3,4,5,])
print(arr)
arr2= np.array([[[1,2,3],[4,5,6],[7, 8, 9]]])
print(arr2)
print(arr2.ndim)

arr3= np.array([1,2,3,4,5,5,6])
print(arr3[2])
print(arr3[5])
x = arr3[2] + arr3[5]
print(x)
arr2d= np.array([[2,3,4,5],[6,7,8,9]])
print(arr2d[0,2])