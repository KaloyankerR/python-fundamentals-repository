tier = {}

tokens = input()

while tokens != "Season end":
    if "vs" in tokens:
        tokens = tokens.split(" vs ")
        first_player = tokens[0]
        second_player = tokens[1]

        if first_player in tier and second_player in tier:
            common_position = [x for x in tier[first_player] if x in tier[second_player]]

            if len(common_position) > 0:
                first_player_skills = 0
                second_player_skills = 0

                for (k, v) in tier[first_player].items():
                    first_player_skills += v

                for (k, v) in tier[second_player].items():
                    second_player_skills += v

                if first_player_skills > second_player_skills:
                    del tier[second_player]
                elif first_player_skills < second_player_skills:
                    del tier[first_player]

    else:
        tokens = tokens.split(" -> ")
        player = tokens[0]
        position = tokens[1]
        skill = int(tokens[2])

        if player not in tier.keys():
            tier[player] = {}

        if position in tier[player].keys():
            if skill < tier[player][position]:
                tier[player][position] = skill
        else:
            tier[player][position] = skill

    tokens = input()

tier_skills = {}
for (k, v) in tier.items():
    v = dict(v)
    total_skills = 0

    for (x, y) in v.items():
        total_skills += y

    tier_skills[k] = total_skills

tier_skills = dict(sorted(tier_skills.items(), key=lambda x: (-x[1], x[0])))
for (k, v) in tier_skills.items():
    print(f"{k}: {v} skill")

    tier_sorted = dict(sorted(tier[k].items(), key=lambda x: (-x[1], x[0])))
    for (x, y) in tier_sorted.items():
        print(f"- {x} <::> {y}")
