list1 = [1,2,3]
list2 = [4,5,6]
print(list1)
print(list2)

list1 += list2

print(list1)
print(list2)

print("----------------------------")

numbers = list(range(3))
print(numbers)

print("----------------------------")

numbers = [10] * 5
print(numbers)

print("----------------------------")

#doesnt return a list. returns each number / element in a new line because of the for loop
numbers = list(range(1, 10, 2))
for n in numbers:
    print(n)

print("----------------------------")

numbers = [1, 2, 3, 4, 5]
print(numbers[-2])

print("----------------------------")

list = [1,2,3,4,5]
sliced_list = list[1:3]
print(sliced_list)
#output = [2,3]

print("----------------------------")

nums = [1,2,3,4,5,6]
print(nums)
print(nums[-2:])

print("----------------------------")

numbers = [1, 2, 3, 4, 5]
my_list = numbers[1:]
print(my_list)

print("----------------------------")

numbers = [1, 2, 3, 4, 5]
my_list = numbers[:1]
print(my_list)

print("----------------------------")

numbers = [1, 2, 3, 4, 5]
my_list = numbers[:]
print(my_list)

print("----------------------------")
list1 = [1,2,3,4]
list2 = list1
list1.append(5)
print(list1)
print(list2)
list2.remove(5)
print(list1)
print(list2)

print("----------------------------")

s = "1234,53,67389"
try:
    a,b = s.split(',') # won't work, too few variables
    a,b,c,d = s.split(',') # won't work, too many variables
except:
    print("variables do not line up")
a,b,c = s.split(",")
print(a,b,c)