#copying a string
'''
s = "hello"
t = s
print(t)
'''


'''
s = "hello"
s[2] = "X"
print(s)
#doesnt work because strings are immutable. Cant change the string.
'''

'''
s = "hello"
t = "goodbye"
u = s + t
print(u)
exit()
'''


'''
s = "hello"
u = ""
for i in range(0, len(s)):
    u = u + s[i]
print(u)
'''


'''
s = "goodbye"
#slice
t = s[3:6]   #3 -5  [beginning index : ending index (not inclusive)]
print(t)
'''

t = "   hello"