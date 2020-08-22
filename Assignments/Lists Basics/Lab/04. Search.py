n = int(input())
word = input()

sentences_list = []
word_list = []
for i in range(n):
    sentence = input()
    sentences_list.append(sentence)

    if word in sentence:
        word_list.append(sentence)

print(sentences_list)
print(word_list)
