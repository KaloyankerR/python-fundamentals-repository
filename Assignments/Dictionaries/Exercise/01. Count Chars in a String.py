word = input()
characters = {}

for letter in word:
    if letter != " ":
        if letter not in characters.keys():
            characters[letter] = 1
        else:
            characters[letter] += 1


for (key, value) in characters.items():
    print(f"{key} -> {value}")
