word_to_remove = input()
sequence = input()

while word_to_remove in sequence:
    sequence = sequence.replace(word_to_remove, '')
print(sequence)
