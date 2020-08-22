employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students_count = int(input())
employee_worked = employee1 + employee2 + employee3
hour = 0

while students_count > 0:
    hour += 1

    if hour % 4 != 0:
        students_count -= employee_worked

print(f"Time needed: {hour}h.")
