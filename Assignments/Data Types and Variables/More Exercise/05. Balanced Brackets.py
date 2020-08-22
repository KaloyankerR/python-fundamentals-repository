n = int(input())

open = False
balanced = True
for i in range(n):
    letter = input()

    if open:
        if letter == ')':
            open = False
        continue

    if letter == '(':
        open = True
    if letter == ')':
        balanced = False

if not open and balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
