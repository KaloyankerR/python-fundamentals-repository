def characters_between(start: str, end: str):
    start = ord(start)
    end = ord(end)
    if start < end:
        for letter in range(start + 1, end):
            print(chr(letter), end=' ')
    else:
        for i in range(end + 1, start, -1):
            print(chr(i), end=' ')


a = input()
b = input()
characters_between(a, b)
