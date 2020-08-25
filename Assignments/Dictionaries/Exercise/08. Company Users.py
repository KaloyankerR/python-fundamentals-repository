companies_dict = {}
tokens = input()

while tokens != "End":
    tokens = tokens.split(" -> ")
    company = tokens[0]
    employee_id = tokens[1]

    if company not in companies_dict.keys():
        companies_dict[company] = []

    if employee_id not in companies_dict[company]:
        companies_dict[company].append(employee_id)

    tokens = input()

ordered_companies = dict(sorted(companies_dict.items(), key=lambda x: x[0]))
for (k, v) in ordered_companies.items():
    print(k)
    for i in v:
        print(f"-- {i}")
