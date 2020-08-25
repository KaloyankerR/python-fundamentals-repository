special_words = input().split(', ')
words = input()

res = list(filter((lambda x: x in words), special_words))
print(res)
