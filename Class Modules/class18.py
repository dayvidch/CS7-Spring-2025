'''
L = [6,2,8,13,3]
print(L)
L[2] += 1
print(L)
for x in L:
    print(x)
'''

'''
k=[]
k.append(int(input("eneter an in: ")))
print(k)

L = [3,4,6,7]
L.append(44)
print(L)
'''

'''
#read some number of numbers from the user
m=[]
x = input("enter a number or 0 to stop\n")
while x != 0:
    m.append(int(x))
    x = input("enter a number or 0 to stop\n")
print(m)


# this is 2x slower because first you are asking if it is true, then if it is not 0
m = []
while True:
    x = int(input("enter a number or 0 to stop"))
    if x == 0:
        break
    m.append(int(x))
print(m)

m.insert(2,22)
print(m)
'''

d = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
