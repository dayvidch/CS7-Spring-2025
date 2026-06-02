# PA2, CS 7 - Introduction to Computer Programming Concepts, 2/15/25


#part 1 
temperature = input("What is the temperature in fahrenheit? ")
temperature = int(temperature)
raining = input("is it raining? ")

if temperature > 90:
    if raining.lower() == "yes":
        print("Wear a swimsuit")

elif temperature > 75:
    print("No coat is needed.")

elif 32 <= temperature <= 75:
    print("Wear a light jacket.")

elif temperature < 32:
    print("Wear a winter coat.")

if raining.lower() == "yes":
    print("Bring an umbrella.")


#part 2
amount = input("Enter a principal amount, in dollars and cents. ")
rate = input("Enter the annual intrest rate. ")

amount = float(amount)
rate = float(rate) * .01

annual_compound = amount * rate
annual_compound = round(annual_compound, 2)

annual_compound_total = amount + annual_compound
annual_compound_total = round(annual_compound_total, 2)

print(f"{'interest compounded annually:':<30}{format(annual_compound, '>15.2f',)}$")
print(f"{'YE balance:':<30}{format(annual_compound_total, '>15.2f')}$")

daily_compound =  amount * (1 + (rate/365))**365 - amount
daily_compound = round(daily_compound, 2)
daily_compound = round(daily_compound, 2)

daily_compound_total = amount + daily_compound
daily_compound_total = round(daily_compound_total, 2)

print(f"{'interest compounded daily:':<30}{format(daily_compound, '>15.2f')}$")
print(f"{'YE balance:':<30}{format(daily_compound_total, '>15.2f')}$")

#part 3
import math

height = input("enter height in inches: ")
width = input("enter width in inches: ")

height = float(height)
width = float(width)

height = height**2
width = width**2

diagonal = height + width
diagonal = math.sqrt(diagonal)
diagonal = round(diagonal, 2)

print("you have a " + str(diagonal) + " inch TV.")


#part4
import random

dice1 = random.randrange(1,7)
dice2 = random.randrange(1,7)
total = dice1 + dice2

print("Dice 1:", str(dice1))
print("Dice 2:", str(dice2))
print("Total:", total)


if total == 2 or total == 3 or total == 12:
    print("You have lost the game")

elif total == 7 or total == 11:
    print("You have won the game")

else:
    point = total
    print("You have scored a point. Your point is =", point)

    dice3 = random.randrange(1,7)
    dice4 = random.randrange(1,7)
    total = dice3 + dice4

    print("Dice 1:", str(dice3))
    print("Dice 2:", str(dice4))
    print("Total:", total)

    if point == total:
        print("You have won the game")

    else:
        print("You have lost the game")