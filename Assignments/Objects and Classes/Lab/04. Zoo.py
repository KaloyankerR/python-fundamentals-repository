class Zoo:
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

    def get_info(self, species):
        if species == 'mammal':
            return f'Mammals in {self.name}: {", ".join(self.mammals)}'

        elif species == 'fish':
            return f'Fishes in {self.name}: {", ".join(self.fishes)}'

        elif species == 'bird':
            return f'Birds in {self.name}: {", ".join(self.birds)}'


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
total_animals = 0
for i in range(count):
    tokens = input().split(' ')
    species = tokens[0]
    animal = tokens[1]
    zoo.add_animal(species, animal)
    total_animals += 1

info = input()
print(zoo.get_info(info))
print(f'Total animals: {total_animals}')