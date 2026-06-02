# PA3, CS 7 - Introduction to Computer Programming Concepts, 2/26/25,

import math

print("---------- Section 1 ---------")
for x in range(0,11):
    if x == 8:
        print("")
    else:
        print(x, x**2, math.sqrt(x))


print("---------- Section 2 ---------")
x = 1
while x < 11:
    if x == 8:
        print("")
    else:
        print(x, x**2, math.sqrt(x))
    x += 1


print("---------- Section 3 ---------")
total = 0
for x in range(30,41):
    total += x
print("total =", total)


print("---------- Section 4 ---------")
lower = input("enter a lower bound: ")
upper = input("enter an upper bound: ")
lower = int(lower)
upper = int(upper)

total = 0
for x in range(lower, upper+1):
     total += x

print("lower:", str(lower))
print("upper:", str(upper))
print("total:", total)


print("---------- Section 5 ---------")
while True:
    userInput =int(input("Enter a number: "))

    if userInput < 0:
        print("done")
        break
    elif userInput == 1:
        print("Dagny")
    elif userInput == 2:
        print("Hank")
    elif userInput == 3:
        print("Francisco")
    else:
        print("ERROR")


print("---------- Section 6 ---------")
while True:
    userInput = input("Enter the name Bob: ")

    if userInput == "Bob":
        print("success")
        break
    else:
        print("ERROR, try again")


print("---------- Section 7 ---------")
while True:
    userInput = input("Enter the name Bob or Amy: ")

    if userInput == "Bob" or userInput == "Amy":
        print("success")
        break
    else:
        print("ERROR, try again")


print("---------- Section 8 ---------")
while True:
    userInput = input("Enter the name Bob or Amy or Ted: ")

    if userInput == "Bob" or userInput == "Amy" or userInput == "Ted":
        print("success")
        break
    else:
        print("ERROR, try again")