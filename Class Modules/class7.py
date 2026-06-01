'''
Python doesnt round the normal way,
they ise gaussian rounding
'''

# x = 4.5
# print(round(x))

''' 
Gaussian Rounding / Bankers Rounding
round to the nearest even number to get rid of bias. 
Round up 2% more of the time
'''


import random
x = random.randint(0,100)
print(x)

#random number between 0 - 1
y = random.random()
print(y)

n = "name"
print(format(n, '^10s')) # center juestified
