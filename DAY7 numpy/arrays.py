import numpy as np
print(np.__version__)
arr1=np.array(["chaitanya"])
print(arr1)

#to check the dimension of the array
print(arr1.ndim)
#2d array
arr2=np.array([[1,2],[3,4],[5,6]])
print(arr2.ndim)
arr3=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr3.ndim)
#3d array
arr4=np.array([[[1,2,3,4],[5,6,7,8],[8,7,6,5]]])
print(arr4.ndim)
print(arr4.shape)
arr5=np.array([[[1,2,3,4],[5,6,7,8],[8,7,6,5]],
               [[12,32,53,4],[95,66,97,58],[28,57,66,85]],
               [[4,6,7,1],[7,1,2,6],[4,1,8,9]]])
#print(arr5)
print(arr5[0,0,0])
