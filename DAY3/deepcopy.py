import copy

list = [1, 2, 3, 4, 5, 6]
list1 = copy.deepcopy(list)
list1[0] = 41
print(list)
print(list1)