row_1 = input().split(' ')
row_2 = input().split(' ')
row_3 = input().split(' ')

case_1 = row_1[0] == row_2[0] == row_3[0]
case_2 = row_1[1] == row_2[1] == row_3[1]
case_3 = row_1[2] == row_2[2] == row_3[2]

case_4 = len(set(row_1)) == 1
case_5 = len(set(row_2)) == 1
case_6 = len(set(row_3)) == 1

case_7 = row_1[0] == row_2[1] == row_3[2]
case_8 = row_1[2] == row_2[1] == row_3[0]

if case_1:
    if row_1[0] == '1':
        print('First player won')
    elif row_1[0] == '2':
        print('Second player won')
    else:
        print('Draw!')
elif case_2:
    if row_1[1] == '1':
        print('First player won')
    elif row_1[1] == '2':
        print('Second player won')
    else:
        print('Draw!')
elif case_3:
    if row_1[2] == '1':
        print('First player won')
    elif row_1[2] == '2':
        print('Second player won')
    else:
        print('Draw!')
elif case_4:
    if row_1[0] == '1':
        print('First player won')
    elif row_1[0] == '2':
        print('Second player won')
    else:
        print('Draw!')
elif case_5:
    if row_2[0] == '1':
        print('First player won')
    elif row_2[0] == '2':
        print('Second player won')
    else:
        print('Draw!')
elif case_6:
    if row_3[0] == '1':
        print('First player won')
    elif row_3[0] == '2':
        print('Second player won')
    else:
        print('Draw!')
elif case_7:
    if row_1[0] == '1':
        print('First player won')
    elif row_1[0] == '2':
        print('Second player won')
    else:
        print('Draw!')
elif case_8:
    if row_1[2] == '1':
        print('First player won')
    elif row_1[2] == '2':
        print('Second player won')
    else:
        print('Draw!')
else:
    print('Draw!')
