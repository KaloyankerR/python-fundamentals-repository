def filter_word(word: str):
    res = []
    digits = ''
    strings = ''
    symbols = ''

    for letter in word:
        if letter.isdigit():
            digits += letter
        elif letter.isalpha():
            strings += letter
        else:
            symbols += letter

    return [digits, strings, symbols]


word = input()
print('\n'.join(filter_word(word)))
