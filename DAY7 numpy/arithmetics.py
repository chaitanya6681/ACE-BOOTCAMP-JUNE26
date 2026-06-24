#Arithmetics (operations and functions)

#scalar arithmetics(operations perform using a single value)
import numpy as np
arr=np.array([1,2,3,4,5])
print("Multiplication of elements:",arr*2)
print("Addition of elements:",arr+5)
print("Subtraction of elements:",arr-2)
print("Division of elements:",arr/2)
print("Modulus of elements:",arr%2)

#scalar Arithmetic Functions
print(np.add(5,arr))
print(np.divide(2,arr))
print(np.multiply(2,arr))
print(np.subtract(2,arr))
print(np.mod(2,arr))


print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.sqrt(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))
