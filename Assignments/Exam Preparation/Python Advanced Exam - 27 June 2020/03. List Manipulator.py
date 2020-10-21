from collections import deque


def list_manipulator(numbers, *args):
    numbers = deque(numbers)
    action = args[0]
    direction = args[1]

    if action == 'add':
        parameters = [int(x) for x in args[2:]]
        if direction == 'beginning':
            [numbers.appendleft(x) for x in parameters[::-1]]
        elif direction == 'end':
            [numbers.append(x) for x in parameters]

    elif action == 'remove':
        parameter = None
        if len(args) == 3:
            parameter = int(args[2])

        if parameter:
            if parameter >= len(numbers):
                numbers.clear()
            else:
                if direction == 'beginning':
                    [numbers.popleft() for x in range(parameter)]
                elif direction == 'end':
                    [numbers.pop() for x in range(parameter)]
        else:
            if direction == 'beginning':
                numbers.popleft()
            elif direction == 'end':
                numbers.pop()

    return [int(x) for x in numbers]


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
