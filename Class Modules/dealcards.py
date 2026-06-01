
import random
deck = []
hand = []

for x in range(1, 53):
    deck.append(x)

for x in range(5):
    card_index = random.randint(0,len(deck)-1)
    card = deck.pop(card_index)
    hand.append(card)

print("deck: ")
print(deck)

print("hand: ")
print(hand)


if card in hand:
    index = deck.index(card)

    if index >= 52:
        suit = "hearts"

    if index >= 39:
        suit = "clubs"

    if index >= 26:
        suit = "diamonds"

    if index >= 13:
        suit = "hearts"

print(suit)





        