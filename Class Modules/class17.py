#finding biggest element
List = [1,2,10,3,4,5]
Largest_so_far = List[0]

for i in range(1,len(List)):
    if List[i] > Largest_so_far:
        Largest_so_far = List[i]
print(Largest_so_far)

#python built in function that does the same thing
print(max(List))
#watch out for boundary conditions


#sorting
m = [4,7.8,1,True,False,-1]  # True and 1 have the same value, which is 1. So the order is how it was found in the original list.
m.sort()
print(m)

m = [4,7.8,True,1,False,-1]  # So then, everything that has equal value will be sorted from what came first.
m.sort()
print(m)


# Linear search -> searching for a given value
# this is some bullshit method
nameList = ["fiona", "lip", "ian","debbie", "carl", "liam", "frank"]
name = input("enter a name: ")
f = False
i = 0

while f == False and i < len(nameList):
    if name == nameList[i]:
        f = True
    else:
        i +=1
if f == True:
    print("yes")
else:
    print("no")

# .contains - built in function

# this one is better
if name in nameList:
    print("yes")
else:
    print("no")

