#file processing
file = open("/Users/david/Code/CS7/asd.txt", "r")
# r = read, w = write, a = append

s = file.read()                 #reads the files and puts it into variable s
print(len(s))                   #prints lenght (number of characters) of the file
print(s)                        #prints it out
file.close()                    #closes the file


file = open("/Users/david/Code/CS7/asd.txt", "r")
s = file.readline()             #reads the first line
print(len(s))
print(s)
file.close()


file = open("/Users/david/Code/CS7/asd.txt", "r")
s = file.readline()
while len(s) != 0:              #loop to print out all the lines of the file
    s = s.rstrip()
    print(s)
    s = file.readline()
file.close()


file = open("/Users/david/Code/CS7/asd.txt", "r")
for s in file:
    s = s.rstrip()
    print(s)
