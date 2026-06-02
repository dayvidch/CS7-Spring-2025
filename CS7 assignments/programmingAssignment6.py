# PA6, CS 7 - Introduction to Computer Programming Concepts, 4/1/25
A6SP25data = open("A6SP25data.txt", "r")

rater_information = A6SP25data.readline()
clean_rater_info = rater_information.rstrip()
rater_info = clean_rater_info.split()
rater_name = rater_info[0] + " " + rater_info[1]

ratings_list = []
resturant_list = []
total_ratings = 0
top_rating = 0

for resturant_ratings in A6SP25data:
    clean_data = resturant_ratings.rstrip()
    rating = int(clean_data[-1])
    resturant = clean_data[:-1]

    ratings_list.append(rating)
    resturant_list.append(resturant)
    total_ratings += 1

    if rating >=4:
          top_rating += 1

average = sum(ratings_list) / total_ratings
average = round(average, 2)

for resturants, ratings in zip(resturant_list, ratings_list):
       print(resturants, "rating:", str(ratings))

print("-----------------------------------------------------")

print(rater_name, "rated", str(total_ratings),"resturants")
print(str(top_rating), "of them recieved top ratings")
print("Average rating:", average)

A6SP25data.close()