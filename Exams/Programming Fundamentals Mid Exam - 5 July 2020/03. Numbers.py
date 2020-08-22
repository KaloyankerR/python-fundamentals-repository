numbers = [int(x) for x in input().split(' ')]
average_number = sum(numbers) / len(numbers)
top_5_numbers = sorted(list(filter((lambda x: x > average_number), numbers)))
top_5_numbers = top_5_numbers[::-1]

if len(top_5_numbers) > 0:
    top_5_numbers = [str(x) for x in top_5_numbers]

    if len(top_5_numbers) > 5:
        top_5_numbers = top_5_numbers[:5]
        print(" ".join(top_5_numbers))
    else:
        print(" ".join(top_5_numbers))
else:
    print("No")
