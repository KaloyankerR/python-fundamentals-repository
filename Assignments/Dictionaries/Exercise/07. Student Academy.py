n = int(input())
students = {}

for ind in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = [grade]
    else:
        students[student_name].append(grade)

filtered_students = {}
for student in students.keys():
    grades = students[student]
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.50:
        filtered_students[student] = average_grade

filtered_students = dict(sorted(filtered_students.items(), key=lambda x: (-x[1])))

for (k, v) in filtered_students.items():
    print(f"{k} -> {v:.2f}")
