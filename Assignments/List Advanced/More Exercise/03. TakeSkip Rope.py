words = [x for x in input()]

digits = list(filter((lambda x: x in '0123456789'), words))
digits = [int(x) for x in digits]

chars = list(filter((lambda x: x not in '0123456789'), words))

take_list = [digits[x] for x in range(0, len(digits)) if x % 2 == 0]
skip_list = [digits[x] for x in range(0, len(digits)) if x % 2 != 0]

index = 0
take = 0
skip = 0
res = []

for i in range(len(take_list)):
    take = take_list[i]

    if take == 0:
        take = ''
    else:
        take = chars[index:index + take]

    index += take_list[i]

    skip = skip_list[i]

    if skip == 0:
        skip = ''
    else:
        skip = chars[index:index + skip]

    index += skip_list[i]

    take = [x for x in take]
    res += ''.join(take)


for word in res:
    print(word, end='')
