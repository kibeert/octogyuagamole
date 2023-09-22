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
print(arr2d.dtype)
arrs = np.array(["apple", "banana", "cherry"], dtype="S")
print(arrs.dtype)

arra =  np.array([1,2,3,4,5])
x =arra.copy()
arra[0] = 12
print(arra)
print(x)
arra2 = np.array([1,2,3,4,5])
y =arra2.view()
arra2[0]= 12
print(arra2)
print(y)
x = arra2.copy()
y = arra2.view()
print(x.base)
print(y.base)
arry2= np.array([[[1,2,3],[4,5,6],[7, 8, 9]]])
print(arry2.shape)
for x in arry2:
    print(x)

for x in arry2:
    for y in x :
        for z in y:
            print(z)

for x in np.nditer(arry2):
    print(x)

array = np.array([1,2,3,4,5])
array3 =np.array([7,8,9,0,12])
a= np.concatenate((array, array3), axis=None)
print(a)
b = np.array_split(a, 3)
print(b)
ar = np.array([1,2,3,4,5,6])
newar = np.array_split(ar, 4)
print(newar)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)
ar = np.array([3,2,1,40,51,6])
x = np.where(ar%2 == 1)
print("The index of the element is ", x )
x = np.sort(ar)
print(x)
arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))
import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))
