word = input()
correct_word = input()

index = 0
for symbol in range(len(word)):
    if word[symbol] != correct_word[symbol]:
        for i in range(0, symbol + 1):
            print(correct_word[i], end='')

        for j in range(symbol + 1, len(word)):
            print(word[j], end='')

        print()
