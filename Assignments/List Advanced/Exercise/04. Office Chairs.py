n = int(input())

chairs_free = 0
is_chairs_free = True
for room in range(1, n + 1):
    chairs_in_rooms = input().split(' ')
    chairs = chairs_in_rooms[0].count('X')
    empty_chairs = chairs - int(chairs_in_rooms[1])

    if empty_chairs >= 0:
        chairs_free += empty_chairs
    else:
        is_chairs_free = False
        print(f'{abs(empty_chairs)} more chairs needed in room {room}')


if is_chairs_free:
    print(f'Game On, {chairs_free} free chairs left')
