def get_snake_position():
    global matrix, n
    for r in range(n):
        if 'S' in matrix[r]:
            for c in range(n):
                if matrix[r][c] == 'S':
                    return [r, c]
                    # get the index with the .index() method


def get_burrows_indexes(field):
    global n
    res = []
    for x in range(n):
        if 'B' in field[x]:
            res.append([x, field[x].index('B')])
    return res


def is_valid(row1, col1, row2, col2):
    global n
    return 0 <= (row1 + row2) < n and 0 <= (col1 + col2) < n


moves = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

n = int(input())
matrix = [[x for x in input()[:n]] for _ in range(n)]
burrows = get_burrows_indexes(field=matrix)
food_quantity = 0

while True:
    row, col = get_snake_position()
    current_move = input()
    next_row, next_col = moves[current_move]

    if not is_valid(row, col, next_row, next_col):
        matrix[row][col] = '.'
        print('Game over!')
        break

    matrix[row][col] = '.'
    next_snake_position = matrix[row + next_row][col + next_col]

    if next_snake_position == '*':
        row, col = row + next_row, col + next_col
        food_quantity += 1
        if food_quantity == 10:
            print('You won! You fed the snake.')
            matrix[row][col] = 'S'
            break

    elif next_snake_position == 'B':
        for burrow in burrows:
            if [row + next_row, col + next_col] != burrow:
                matrix[row + next_row][col + next_col] = '.'
                row, col = burrow

    else:
        row, col = row + next_row, col + next_col

    matrix[row][col] = 'S'

print(f'Food eaten: {food_quantity}')
[print(''.join(x)) for x in matrix]