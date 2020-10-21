from collections import defaultdict

students = defaultdict(list)
n = int(input())

for _ in range(n):
    data = input().split()
    student_name = data[0]
    student_grade = float(data[1])
    students[student_name].append(student_grade)

# students = {x: (sum(y) / len(y)) for (x, y) in students.items()}
for (name, grades) in students.items():
    student_grades = list(map(lambda x: format(x, ".2f"), grades))
    print(f"{name} -> {' '.join(student_grades)} (avg: {sum(grades) / len(grades):.2f})")
