numbers = []
for number in input().split(' '):
    num = list(map((lambda x: int(x)), number))
    numbers.append(sum(num))

words = []
sentence = list(map((lambda x: words.append(x)), input()))

while len(numbers) != 0:
    index = numbers[0]
    words_len = len(words)

    if index >= words_len:
        index -= words_len

    print(words[index], end='')

    numbers.pop(0)
    words.pop(index)
