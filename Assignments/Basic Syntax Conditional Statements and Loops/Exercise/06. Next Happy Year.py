year = int(input()) + 1
year = str(year)

not_happy_year = True

while not_happy_year:
    is_valid = True
    for digit in year:
        if year.count(digit) > 1:
            year = int(year) + 1
            year = str(year)
            is_valid = False
            break

    if is_valid:
        not_happy_year = False
        break

print(year)
