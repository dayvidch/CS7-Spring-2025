# PA1, CS 7 - Introduction to Computer Programming Concepts, 2/1/25


#part1
question1 = input("How many hours did you work last week? ")
question2 = input("What is your hourly wage? ")
payment = float(question1) * float(question2)
print("You earned $" + str(payment))


#part2
question3 = input("Enter the temperature in Fahrenheit: ")
centigrade = float(question3) - 32
centigrade = centigrade * (5/9)
print("That is", centigrade, "in Centigrade")


#part3
id = input("Enter your ID number: ")

item1 = input("Enter your first item: ")
cost1 = float(input("Enter cost of first item: "))

item2 = input("Enter your second item: ")
cost2 = float(input("Enter cost of second item: "))

item3 = input("Enter your third item: ")
cost3 = float(input("Enter cost of third item: "))

subtotal = cost1 + cost2 + cost3

tax = float(subtotal) * 0.1025

total = subtotal + tax

print("----------------Receipt for, id", id, "------------------")
print(item1, str(cost1))
print(item2, str(cost2))
print(item3, str(cost3))
print("subtotal: ", str(subtotal))
print("tax: ", str(tax))
print("total:", str(total))