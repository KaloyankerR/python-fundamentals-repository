sequence = input().split(" ")
dictionary = {}

for var in range(0, len(sequence)):
    if sequence[var].isdigit():
        var = int(sequence[var])

        if var in dictionary.keys():
            dictionary[var] += 1
        else:
            dictionary[var] = 1

    else:
        var = sequence[var].lower()

        if var in dictionary.keys():
            dictionary[var] += 1
        else:
            dictionary[var] = 1

res = [print(x, end=' ') for x in dictionary.keys() if dictionary[x] % 2 != 0]
