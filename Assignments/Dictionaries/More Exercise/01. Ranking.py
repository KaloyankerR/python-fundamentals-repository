contests_and_passwords = {}
candidates = {}
tokens = input()

while tokens != "end of contests":
    tokens = tokens.split(":")
    contest = tokens[0]
    password = tokens[1]
    contests_and_passwords[contest] = password
    tokens = input()

tokens = input()
while tokens != "end of submissions":
    tokens = tokens.split("=>")
    contest = tokens[0]

    if contest in contests_and_passwords.keys():
        password = tokens[1]
        if password == contests_and_passwords[contest]:
            name = tokens[2]
            if name not in candidates.keys():
                candidates[name] = {}

            points = int(tokens[3])
            if contest in candidates[name].keys():
                candidate_points = candidates[name][contest]
                if points > candidate_points:
                    candidates[name][contest] = points
            else:
                candidates[name][contest] = points

    tokens = input()

best_candidate = ""
best_candidate_points = 0
for (k, v) in candidates.items():
    v = dict(v)
    candidate_points = 0

    for (c, p) in v.items():
        candidate_points += p

    if candidate_points > best_candidate_points:
        best_candidate = k
        best_candidate_points = candidate_points

print(f"Best candidate is {best_candidate} with total {best_candidate_points} points.")

ranking_candidates = dict(sorted(candidates.items(), key=lambda x: (x[0])))

print("Ranking:")
for (k, v) in ranking_candidates.items():
    print(k)
    v = dict(v)
    ranking_candidates_contests = dict(sorted(v.items(), key=lambda x: -x[1]))

    for (contest, points) in ranking_candidates_contests.items():
        print(f"#  {contest} -> {points}")
