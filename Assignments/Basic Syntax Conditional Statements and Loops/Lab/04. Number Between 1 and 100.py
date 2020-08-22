MIN = 1
MAX = 100
num = float(input())
while not (1 <= num <= 100):
    num = float(input())

print(f'The number {num} is between {MIN} and {MAX}')
