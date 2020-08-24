def tribonacio_sequence(count):
    numbers = [1]
    for i in range(1, count):
        try:
            numbers.append(sum(numbers[-3::]))
        except IndexError:
            numbers.append(1)

    return numbers


number = int(input())
res = tribonacio_sequence(number)
a = [print(x, end=' ') for x in res]
