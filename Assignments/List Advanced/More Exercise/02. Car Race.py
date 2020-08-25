import math


def time_first_racer(num):
    global total_first_racer

    if num == 0:
        total_first_racer *= 0.8
    else:
        total_first_racer += num


def time_second_racer(num):
    global total_second_racer

    if num == 0:
        total_second_racer *= 0.8
    else:
        total_second_racer += num


car_time = input().split()
car_time_len = math.ceil(len(car_time) / 2)

first_racer = car_time[:car_time_len - 1]
first_racer = [int(x) for x in first_racer]

second_racer = list(reversed(car_time[car_time_len::]))
second_racer = [int(x) for x in second_racer]

total_first_racer = 0
total_second_racer = 0

first_racer_time = list(map(time_first_racer, first_racer))
second_racer_time = list(map(time_second_racer, second_racer))

if total_first_racer <= total_second_racer:
    print(f'The winner is left with total time: {total_first_racer:.1f}')
else:
    print(f'The winner is right with total time: {total_second_racer:.1f}')
