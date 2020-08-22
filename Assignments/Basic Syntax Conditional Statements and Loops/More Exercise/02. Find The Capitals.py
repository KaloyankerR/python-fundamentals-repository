word = input()
index_list = []

for index in range(0, len(word)):
    if word[index].isupper():
        index_list.append(index)

print(index_list)
