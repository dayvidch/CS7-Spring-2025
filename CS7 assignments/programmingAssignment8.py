# PA8, CS 7 - Introduction to Computer Programming Concepts, 5/8/25
import random

# Part 1
five_heads = []
flips = int(input("How many times do you want to flip 5 coins?: "))

def flip5Coins():
    not_heads = 0
    for x in range(5):
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            not_heads += 1

    if not_heads == 0:
        five_heads.append(1)

for x in range(flips):
    flip5Coins()

five_heads = sum(five_heads)

percentage = (five_heads/flips)*100
percentage = round(percentage, 2)

print("We flipped 5 coins", flips, "times")
print(five_heads, "were all heads")
print("thats", percentage, "percent heads")


# Part 2
def rollone():
    roll = random.randint(1,6)
    return roll

total_rolls = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

user_rolls = int(input("enter number of rolls: "))

for x in range(user_rolls):
    roll1 = rollone()
    roll2 = rollone()
    total = roll1 + roll2
    total_rolls[total] += 1

for key in total_rolls:
    print("roll", key, "occurances", total_rolls[key], round((total_rolls[key]/user_rolls)*100, 2), "%")


