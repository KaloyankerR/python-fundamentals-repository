from collections import deque

data = deque(input().split())

all_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
second_colors = ['orange', 'purple', 'green']

colors_to_combine = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}
colors = []

while data:
    first_col = data.popleft()
    if data:
        second_col = data.pop()

        if (first_col + second_col) in all_colors:
            colors.append(first_col + second_col)
        elif (second_col + first_col) in all_colors:
            colors.append(second_col + first_col)
        else:
            first_col = first_col[0:-1]
            second_col = second_col[0:-1]

            if first_col:
                data.insert(len(data) // 2, first_col)
            if second_col:
                data.insert(len(data) // 2, second_col)
        continue

    if first_col in all_colors:
        colors.append(first_col)


for col in colors:
    if col in second_colors:
        not_color = False
        for i in colors_to_combine[col]:
            if i not in colors:
                not_color = True
                break

        if not_color:
            colors.remove(col)

print(colors)