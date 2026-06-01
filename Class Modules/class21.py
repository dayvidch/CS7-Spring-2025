'''double lists'''

doubleList = [[1,1,1],[2,2,2], [3,3,3]]

print(doubleList)

for i in doubleList:
    print(i)

# for i in range(0, doubleList):
#     for j in range(0, doubleList[0]):
#         print(doubleList[i][j])

'''functions'''

'''bubble sort'''
l = [7,5,4,2,1,6,3]
print(l)

for i in range(0, len(l)-1):
    for j in range(0, len(l)-1):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
print(l)