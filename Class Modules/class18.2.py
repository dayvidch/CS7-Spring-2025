'''
L = [1,3,5,7,9]

print(L[2:5])   #slicing

L.reverse()  #reversing the list
print(L)

del L[-1]
print(L)

# del L[33]    #out of range error
# print(L)
'''

L = [1,3,5,7,9]

#try this first
try:
    n = int(input("enter a value to delete: "))
    L.remove(n)
    print(L)
#code that gets executted only when there is a ValueError, catch bad data without blowing up the code
except ValueError:
    print("Thats a bad value")

except IndexError:
    print("")

#exits the try block and moves on to the next line of code. This code will run no matter what
print("ok here we are now")