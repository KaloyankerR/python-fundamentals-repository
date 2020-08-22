def command(a):
    result = []

    if a == 'even':
        for even in numbers:
            if even % 2 == 0:
                result.append(even)

    elif a == 'odd':
        for odd in numbers:
            if odd % 2 != 0:
                result.append(odd)

    elif a == 'negative':
        for negative in numbers:
            if negative < 0:
                result.append(negative)

    elif a == 'positive':
        for positive in numbers:
            if positive >= 0:
                result.append(positive)

    return result


counter = int(input())
numbers = []

for i in range(counter):
    numbers.append(int(input()))

print(command(input()))
