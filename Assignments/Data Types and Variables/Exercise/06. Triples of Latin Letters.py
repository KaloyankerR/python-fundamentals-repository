# С const (по-бавно)
n = int(input())
BEGINNING = 97

for first_chr in range(BEGINNING, BEGINNING + n):
    for second_chr in range(BEGINNING, BEGINNING + n):
        for third_chr in range(BEGINNING, BEGINNING + n):
            print(f'{chr(first_chr)}{chr(second_chr)}{chr(third_chr)}')

# Без const по-бързо
# n = int(input())
# BEGINNING = 97
#
# for first_chr in range(97, 97 + n):
#     for second_chr in range(97, 97 + n):
#         for third_chr in range(97, 97 + n):
#             print(f'{chr(first_chr)}{chr(second_chr)}{chr(third_chr)}')
