users = {}
contests = {}
tokens = input()

while tokens != "no more time":
    tokens = tokens.split(" -> ")
    user = tokens[0]
    contest = tokens[1]
    points = int(tokens[2])

    if contest not in contests.keys():
        contests[contest] = {}

    if user not in contests[contest].keys():
        if user not in users.keys():
            users[user] = 0

        contests[contest][user] = points
        users[user] += points
    else:
        if points > contests[contest][user]:
            users[user] += points - contests[contest][user]
            contests[contest][user] = points

    tokens = input()

for (k, v) in contests.items():
    print(f"{k}: {len(v)} participants")
    v = dict(v)
    participants_sorted = dict(sorted(v.items(), key=lambda x: (-x[1], x[0])))
    number = 1
    for (n, p) in participants_sorted.items():
        print(f"{number}. {n} <::> {p}")
        number += 1

print("Individual standings:")
users_sorted = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
number = 1
for (k, v) in users_sorted.items():
    print(f"{number}. {k} -> {v}")
    number += 1
