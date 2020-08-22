key = int(input())
n = int(input())

letter_key = ''
for i in range(n):
    letter = ord(input())
    letter_key += chr(letter + key)

print(letter_key)
