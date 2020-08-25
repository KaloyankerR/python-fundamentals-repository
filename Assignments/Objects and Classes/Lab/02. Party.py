class Party:
    def __init__(self):
        self.party_people = []
        self.party_people_counter = 0


party = Party()
people = input()

while people != 'End':
    party.party_people.append(people)
    party.party_people_counter += 1

    people = input()

print(f'Going: {", ".join(party.party_people)}')
print(f'Total: {party.party_people_counter}')

