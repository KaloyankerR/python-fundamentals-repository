def progress_bar(percent):
    progressed = percent // 10
    not_progressed = 10 - progressed

    if progressed == 10:
        print(f'{percent}% Complete!')
        print(f'[{"%" * progressed}{"." * not_progressed}]')
    else:
        print(f'{percent}% [{"%" * progressed}{"." * not_progressed}]')
        print('Still loading...')


progress_bar(percent=int(input()))
