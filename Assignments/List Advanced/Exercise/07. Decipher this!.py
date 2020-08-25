def decipher():
    new_words = []

    for word in words:
        integers = []
        strings = []

        for letter in word:
            if letter.isdigit():
                integers.append(str(letter))
            else:
                strings.append(letter)

        first_letter = chr(int(''.join(integers)))

        strings[0], strings[-1] = strings[-1], strings[0]
        strings = ''.join(strings)

        new_word = first_letter + strings
        new_words.append(new_word)

    return ' '.join(new_words)


words = input().split(' ')
print(decipher())
