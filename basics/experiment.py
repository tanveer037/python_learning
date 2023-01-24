list1 = [ [1,2],[3,4] ]
list2 = [[11,22],[33,44]]
list3 = [(list1[i][j],list2[i][j]) for i in range(0,2) for j in range(0,2)]
print(list3)