import sys
list1=[]
for i in range(10):
    list1.append(i)
    print(sys.getsizeof(list1))
print(list1)
print(sys.getsizeof(list1))
print(list.__sizeof__(list1))

list2=[None]*10
print(sys.getsizeof(list2))
for i in range(10):
    list2[i]=i
    print(sys.getsizeof(list2))
print(list2)