counter = int(input())
dictionary = {}

for i in range(counter):
    word = input()
    synonym = input()

    if word in dictionary.keys():
        dictionary[word] += f', {synonym}'
    else:
        dictionary[word] = synonym


for key in dictionary.keys():
    print(f"{key} - {dictionary[key]}")

