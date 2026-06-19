import copy
l=[[1,2,3],[1,1,1],[2,2,4]]
sl=copy.copy(l)
sl[0][0]=100
print(sl)
l[0][0]=200
print(l)
