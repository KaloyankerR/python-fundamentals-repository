import sys

def get_bunny_position():
    global matrix
    for _ in range(n):
        if 'B' in matrix[_]:
            return [_, matrix[_].index('B')]


n = int(input())
matrix = [input().split() for x in range(n)]
bunny_position = get_bunny_position()

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

max_value = -sys.maxsize
max_value_side = ''
max_value_positions = []

while True:
    current_row, current_col = bunny_position
    for move in moves.keys():
        r, c = moves[move]

        row, col = current_row, current_col
        value = 0
        positions = []

        while True:
            row += r
            col += c

            if 0 <= row < n and 0 <= col < n:
                if matrix[row][col] == 'X':
                    break
                value += int(matrix[row][col])
                positions.append([row, col])

            else:
                break

        if value > max_value and len(positions) > 0:
            max_value = value
            max_value_side = move
            max_value_positions = positions
    break

if max_value_side != '':
    print(max_value_side)

[print(x) for x in max_value_positions]
print(max_value)
