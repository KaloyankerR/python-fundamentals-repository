banned_words = input().split(", ")
sequence = input()

for word in banned_words:
    if word in sequence:
        sequence = sequence.replace(word, '*' * len(word))

print(sequence)
