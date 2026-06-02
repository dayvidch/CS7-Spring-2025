# PA9, CS 7 - Introduction to Computer Programming Concepts
data = open("titanic.csv", "r")
header = data.readline()

passengers = 0
survived = 0
men_survived = 0 
total_men = 0
women_survived = 0
total_women = 0
children_survived = 0
total_children = 0

for line in data:
    line = line.split(",")
    passengers +=1
    survived += int(line[1])
    #women
    if "female" in line:
        total_women += 1
        if line[1] == "1":
            women_survived += 1
    #men
    if "male" in line:
        total_men += 1
        if line[1] =="1":
            men_survived += 1
    
    #children
    if line[6] == "":
        continue
    if float(line[6]) <= 12:
        total_children += 1
        if line[1] =="1":
            children_survived += 1


total_survived_percent = (men_survived + women_survived) / passengers
total_survived_percent = total_survived_percent*100
total_survived_percent = round(total_survived_percent,2)

men_survived_percentage = (men_survived / total_men)*100
men_survived_percentage = round(men_survived_percentage, 2)

women_survived_percentage = (women_survived / total_women)*100
women_survived_percentage = round(women_survived_percentage, 2)

children_survived_percentage = (children_survived / total_children)*100
children_survived_percentage = round(children_survived_percentage,2)
    
print("passengers:", passengers)
print("passenger survival percentage:", total_survived_percent, "%")
print("men survival percentage:", men_survived_percentage, "%")
print("women survival percentage:", women_survived_percentage, "%")
print("children survival percentage:", children_survived_percentage, "%")
