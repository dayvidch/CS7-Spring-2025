# PA7, CS 7 - Introduction to Computer Programming Concepts, 4/28/25

#gpa calculator function
def gpa_calculator(gradepoint, totalhours):
    gpa = gradepoint / totalhours
    gpa = round(gpa,2)
    print("GPA =", gpa)

# dataset
data = open("/Users/david/Desktop/Code/CS7/CS7 assignments/pa8data.csv", "r")

#student name
student = data.readline()
student = student.split(",")
first_name = student[0]
last_name = student[1]

#Oragnizing data
semester = []
department = []
course = []
hours = []
grades = []

for line in data:
    line = line.split(",")
    semester.append(line[0])
    hours.append(line[1])
    grades.append(line[2])
    department.append(line[3])
    course.append(line[4])

data.close()

#total hours
total_hours = 0 
for hour in hours:
    total_hours += int(hour)

#total gradepoint
gradepoint = 0
for grade in range(len(grades)):
    gp = 0
    if grades[grade] == "A":
        gp+= 4
    elif grades[grade] == "B":
        gp += 3
    elif grades[grade] == "C":
        gp += 2
    elif grades[grade] == "D":
        gp += 1
    else:
        gp += 0
    gradepoint += gp * int(hours[grade])

#printing report
print(first_name, last_name)

#clean line of \n
for c in range(len(course)):
    course[c] = course[c].rstrip()

print(f"{'Semester':<8} {'Department':<10} {'Course':<6} {'Hours':<5} {'Grades':<6}")

for x in range(len(semester)):
    print(f"{semester[x]:<8} {department[x]:<10} {course[x]:<6} {hours[x]:<5} {grades[x]:<6}")

#call to gpa function
gpa_calculator(gradepoint, total_hours)
