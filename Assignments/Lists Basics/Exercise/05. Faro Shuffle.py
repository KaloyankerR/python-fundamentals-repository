cards = input().split(' ')
shuffles = int(input())
index = (len(cards)) // 2

for shuffle in range(shuffles):
    first_deck = cards[:index]
    second_deck = cards[index:]
    new_deck = []

    for i in range(index):
        new_deck.append(first_deck[i])
        new_deck.append(second_deck[i])
    cards = new_deck

print(cards)