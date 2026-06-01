#making dictionary where characters are key, and number is value
characters = {
    "Fionna": 1,
    "Lip": 2,
    "Ian": 3,
    "Debbie": 4,
    "Carl": 5,
    "Liam": 6
}
print(characters)

#changing the value for a specific key
characters["Fionna"] = 10
print(characters)

#adding new key:value pair
#if the key doesnt exist, it adds it to the end of the dictionary
characters["Frank"] = "alcoholic"
print(characters)

#removing a key:value pair by using pop()
#if key isnt found, it returns a deault value
x = characters.pop("Kevin", "not a gallagher")
print(x)
print(characters)

#dont have to set it to avariable, just cant use the popped key:value no more
characters.pop("Fionna")
print(characters)

#del removes a key:value pair, but it causes a keyerror if key is not found
#del characters["Veronica"]

#doing arithetic on a value in a dictionary
print(characters["Lip"])
characters["Lip"] += 2
print(characters["Lip"])
