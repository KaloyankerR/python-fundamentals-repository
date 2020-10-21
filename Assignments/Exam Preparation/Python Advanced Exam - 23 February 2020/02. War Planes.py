def get_start_position():
    global matrix, n

    for r in range(n):
        if 'p' in matrix[r]:
            return [r, matrix[r].index('p')]


def get_target_count():
    global matrix
    count = 0
    for r in range(len(matrix)):
        count += matrix[r].count('t')

    return count


def is_valid_index(r: int, c: int, nxt_r: int, nxt_c: int):
    global n

    return 0 <= (r + nxt_r) < n and 0 <= (c + nxt_c) < n


def get_direction(dir: str, val: int):
    directions = {
        'up': [-val, 0],
        'down': [val, 0],
        'right': [0, val],
        'left': [0, -val]
    }
    return directions[dir]


n = int(input())
matrix = [[c for c in input().split()] for r in range(n)]
target_count = get_target_count()
target_count_copy = target_count

player_position = get_start_position()


m = int(input())
is_accomplished = False

for _ in range(m):
    data = input().split()
    cmd = data[0]
    next_row, next_col = get_direction(data[1], int(data[2]))
    player_row, player_col = player_position

    if is_valid_index(player_row, player_col, next_row, next_col):
        if cmd == 'move':
            if matrix[player_row + next_row][player_col + next_col] == '.':
                matrix[player_row][player_col] = '.'
                player_row += next_row
                player_col += next_col
                matrix[player_row][player_col] = 'p'
                player_position = [player_row, player_col]

        elif cmd == 'shoot':
            if matrix[player_row + next_row][player_col + next_col] == 't':
                matrix[player_row + next_row][player_col + next_col] = 'x'
                target_count -= 1
                if target_count == 0:
                    is_accomplished = True
                    break
            else:
                matrix[player_row + next_row][player_col + next_col] = 'x'


if is_accomplished:
    print(f'Mission accomplished! All {target_count_copy} targets destroyed.')
else:
    print(f'Mission failed! {target_count} targets left.')


for r in matrix:
    print(' '.join(r))
