array = [int(x) for x in input().split(' ')]
tokens = input()

while tokens != "end":
    tokens = tokens.split(' ')
    command = tokens[0]

    if command == "swap":
        index1 = int(tokens[1])
        index2 = int(tokens[2])

        array[index1], array[index2] = array[index2], array[index1]

    elif command == "multiply":
        index1 = int(tokens[1])
        index2 = int(tokens[2])

        multiplied_value = array[index1] * array[index2]
        array[index1] = multiplied_value

    elif command == "decrease":
        array = list(map((lambda x: x - 1), array))

    tokens = input()

array_str = [str(x) for x in array]
print(", ".join(array_str))
