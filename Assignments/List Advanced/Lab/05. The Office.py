employees = [int(x) for x in input().split(' ')]
factor =int(input())

employees_mapping = list(map((lambda x: x * factor), employees))
employees_happiness = sum(employees_mapping) / len(employees)
employees_filtered = list(filter((lambda x: x >= employees_happiness), employees_mapping))
happy_employees = len(employees_filtered)

if happy_employees >= (len(employees) // 2):
    print(f'Score: {happy_employees}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {happy_employees}/{len(employees)}. Employees are not happy!')
