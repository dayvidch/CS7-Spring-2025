# PA4, CS 7 - Introduction to Computer Programming Concepts, 3/12/25
import random

#Part 1
all_heads = 0
not_all_heads = 0
flips = 1000

for x in range(flips):
    coin1 = random.randrange(0,2)
    coin2 = random.randrange(0,2)
    coin3 = random.randrange(0,2)
    coin4 = random.randrange(0,2)

    if coin1 == 0 and coin2 == 0 and coin3 == 0 and coin4 == 0:
        all_heads += 1
    else:
        not_all_heads += 1

print("number of flips:", flips)
print("number of all heads",all_heads)
print("number of not all heads", not_all_heads)
print("percentage of all heads", ((all_heads/flips)*100),"%")


#Part 2
username = input("Provide your names in terms of: last name, first name, and middle name: ")
parsed_username = username.split(",")
# print(parsed_username)

print("first name:", parsed_username[1])
print("middle name:", parsed_username[2])
print("last name:", parsed_username[0])


#Part 3
random_number = random.randrange(1,101)
print("I have generated a random number 1-100")

game_done = False
guesses = 0
while game_done == False:
    user_guess = int(input("guess the number: "))
    if user_guess > random_number:
        print("too high, guess again")
    elif user_guess < random_number:
        print("too low, guess again")
    else:
        print("correct")
        print("guesses:",guesses)
        game_done = True
    guesses += 1