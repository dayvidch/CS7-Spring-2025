#integer and float arithmetic are different

#truncate

n1 = 6
n2 = 2

n3 = n1/n2
print(type(n3), n3)     #this gives a float data type

#integer division
#if you have 2 floats, but want an integer answer, then use integer division //
n3 = n1//n2     #this gives out a integer data type
print(type(n3), n3)
