longest_intersection = [[]]

for i in range(int(input())):
    data = input().split("-")
    first_start, first_end = list(map(int, data[0].split(",")))
    second_start, second_end = list(map(int, data[1].split(",")))

    first = set(x for x in range(first_start, first_end + 1))
    second = set(x for x in range(second_start, second_end + 1))

    intersection = first.intersection(second)

    if len(intersection) > len(longest_intersection[0]):
        longest_intersection.clear()
        longest_intersection.append(list(intersection))

print(f"Longest intersection is {longest_intersection[0]} with length {len(longest_intersection[0])}")
