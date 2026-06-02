# PA5, CS 7 - Introduction to Computer Programming Concepts, 3/30/25

List = []
x = 0
while x != -1:
    x = int(input("enter a number: "))
    List.append(x)
else:
    List.pop()
    print(List)
    print("sum:", sum(List))
    print("average:", sum(List)/len(List))

for x in range(2):
    target_integer = int(input("enter a target integer: "))
    if target_integer in List:
        print("yes")
    else:
        print("no")
        List.append(target_integer)
print("current list: ", List)   

name_list = []
names = input("enter a set of names in one line, seperated by commas: ")
name_split = names.split(",")
for name in name_split:
    stripped_name =name.strip()
    name_list.append(stripped_name)
print(name_list)

for x in range(2):
    user_name = input("enter a name: ")
    user_name = user_name.strip()

    if user_name in name_list:
        name_list.remove(user_name)
    else:
        print("name not in list")
print(name_list)