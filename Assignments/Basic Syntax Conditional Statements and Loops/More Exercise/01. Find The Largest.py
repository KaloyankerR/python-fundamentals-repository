number = reversed(sorted(input()))

largest_number = ''
for digit in number:
    largest_number += digit

print(largest_number)
