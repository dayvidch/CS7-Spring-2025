'''
students = {12345: "Mikey", 6789: "Lip", 9876: "Carl", 54321: "Ian"}

print(students)

#making query of dictonary
#user_input = int(input("eneter key:"))

if user_input in students:
    data = students[user_input]          #retrevial
    print(data)
else:
    print("not found")

#pythonic way

data = students.get(user_input, "____zizzy xyz")
if data == "None":
    print(data)

#clears the dictionary
students.clear()
print(students)
key,value = input("enter key and value")
key = int(key)
students[key] = value
print(students)

'''
def lookup_day():
    days = {
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6,
        "Saturday": 7
    }
    n = days.get(dayname, "sorry that was invalid")
    return n

dayname = input("enter day name: ")
k = lookup_day(dayname)
print(k)