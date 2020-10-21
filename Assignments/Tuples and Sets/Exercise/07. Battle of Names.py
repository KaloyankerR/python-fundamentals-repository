even = set()
odd = set()

for i in range(1, int(input()) + 1):
    name_sum = sum([ord(x) for x in input()]) // i

    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

if sum(even) == sum(odd):
    arg = list(map(str, even.union(odd)))
    print(", ".join(arg))
elif sum(even) < sum(odd):
    arg = list(map(str, odd.difference(even)))
    print(", ".join(arg))
elif sum(even) > sum(odd):
    arg = list(map(str, even.symmetric_difference(odd)))
    print(", ".join(arg))
