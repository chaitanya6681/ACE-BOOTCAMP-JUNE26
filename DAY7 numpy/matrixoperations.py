import numpy as np
arr=np.array([[1,2],[3,4]])
arr1=np.array([[1,2],[3,4]])
arr1.flags.writeable=False
marks=np.array([[96,98,54,43,12],
                 [65,78,89,90,1]])
marks[(marks>50)&(marks<=70)]=4
print(marks)
print("Addition is : \n",arr+arr1)
print("Multiplication is : \n",arr @ arr1)
print("Multiplication is : \n",np.matmul(arr,arr1))
#print("Comparision :",marks[0::marks>45])
