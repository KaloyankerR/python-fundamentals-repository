A = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
B = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

is_less = False
cards = input().split(' ')
for card in cards:
    card = card.split('-')
    team = card[0]
    number = card[1]

    if team == "A":
        try:
            A.remove(number)

        except ValueError:
            pass

    elif team == 'B':
        try:
            B.remove(number)

        except ValueError:
            pass

    if len(A) < 7 or len(B) < 7:
        is_less = True

print(f'Team A - {len(A)}; Team B - {len(B)}')
if is_less:
    print('Game was terminated')
