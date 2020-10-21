from collections import deque

expression = input().split()
numbers = deque()

for element in expression:
    try:
        element = int(element)
        numbers.append(element)
    except ValueError:
        res = numbers.popleft()

        if element == '+':
            for num in numbers:
                res += num
        elif element == '-':
            for num in numbers:
                res -= num
        elif element == '*':
            for num in numbers:
                res *= num
        elif element == '/':
            for num in numbers:
                if num != 0 and res != 0:
                    res //= num
                else:
                    res = 0

        numbers.clear()
        numbers.append(res)

print(numbers[0])
