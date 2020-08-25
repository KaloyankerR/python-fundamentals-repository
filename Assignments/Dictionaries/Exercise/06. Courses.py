args = input()
courses = {}

while args != "end":
    args = args.split(" : ")
    course = args[0]
    name = args[1]

    if course in courses.keys():
        courses[course].append(name)
    else:
        courses[course] = [name]
    args = input()

courses_sorted = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
for (k, v) in courses_sorted.items():
    print(f"{k}: {len(v)}")
    for i in sorted(v):
        print(f"-- {i}")
