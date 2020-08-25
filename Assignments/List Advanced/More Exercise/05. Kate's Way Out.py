def maze_append():
    maze_list = []
    for i in range(rows):
        row = input()
        row = [x for x in row]
        maze_list.append(row)
    return maze_list


def kate_position_in_maze():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'k':
                return [i, j]


rows = int(input())

maze = maze_append()

kate_position = kate_position_in_maze()


while True:
    i = kate_position[0]

    # if
    pass