n, m = list(map(int, input().split()))
first_set = set([int(input()) for x in range(n)])
second_set = set([int(input()) for x in range(m)])
[print(x) for x in (first_set.intersection(second_set))]
