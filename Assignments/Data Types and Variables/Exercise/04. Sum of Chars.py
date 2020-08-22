n = int(input())

sum_letters = 0
for char in range(n):
    letter = input()
    sum_letters += ord(letter)

print(f'The sum equals: {sum_letters}')
