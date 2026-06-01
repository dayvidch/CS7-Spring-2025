'''
name = input("What is your name? ")

gas = float(input("How many gallons of gas did you buy? "))

price = float(input("How much did you pay for gallon? "))

money = gas * price

print("Hello " + name)
print("You got "+ str(gas) + " gallons at " + str(price) + " per gallon, for a total of $" + str(money))
'''

import math

n = input("enter a number: ")
n = float(n)
print(math.sqrt(n))       #squareroot function

print(math.sqrt(n)* math.sqrt(n))     #doesnt give out the exact answer because of rounding


