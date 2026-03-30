data = [7,9,1,3,3,1,2,3,3,2,4,1,2]
'''
data.sort()

seen = [data[0]]
unique = 0
for i in range(1, len(data)-1):         #start at element 2, so index 1
    if data[i] != seen[unique]:
        seen.append(data[i])
        unique += 1
print(seen)

#create a list of counters
count = []
for i in range(0, len(seen)):
    count.append(0)

#count occurances
for i in data:
    for unique in range(0,len(seen)):
        if i == seen[unique]:
            count[unique] +=1
print(count)

#find the biggest number in counts
largestsofar = count[0]
savedindex = 0
for i in range(1, len(count)):
    if count[i] > largestsofar:
        largestsofar = count[i]
        savedindex = i
print(largestsofar, savedindex)

print("mode =", seen[savedindex])
'''

#pythonic way

#unique values
seen = set(data)
seen = list(seen)
print(seen)

#list of counters
counts = [0 for n in range(0,len(seen))]

#count values
for i in data:
    y = seen.index(i)
    counts[y] += 1

y = max(counts)
z = seen.index(y)
print("mode =", z)