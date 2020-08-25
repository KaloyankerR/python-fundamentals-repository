strings = input().split(" ")

for word in strings:
    print(word * len(word), end='')
