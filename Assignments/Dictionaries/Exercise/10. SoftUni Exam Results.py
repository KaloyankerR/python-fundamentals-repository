results = {}
submissions = {}
tokens = input()

while tokens != "exam finished":
    tokens = tokens.split("-")
    user = tokens[0]
    language = tokens[1]

    if language == "banned":
        results.pop(user)

    else:
        points = int(tokens[2])

        if user in results.keys():
            if points >= results[user]:
                results[user] = points
        else:
            results[user] = points

        if language not in submissions.keys():
            submissions[language] = 1
        else:
            submissions[language] += 1
    tokens = input()

sorted_results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
print("Results:")
for (k, v) in sorted_results.items():
    print(f"{k} | {v}")

sorted_submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))
print("Submissions:")
for (k, v) in sorted_submissions.items():
    print(f"{k} - {v}")
