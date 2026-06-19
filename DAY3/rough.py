l=[[1,2,3],[1,1,1],[2,2,4]]
l1=[[1,2,3],[1,1,1],[2,2,4]]
print(l+l1)
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j]*l1[i][j],end=" ")