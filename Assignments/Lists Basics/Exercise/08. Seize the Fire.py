fires_with_cells = input().split('#')
water = int(input())
put_on_cells = []
total_fire = 0
effort = 0

for i in fires_with_cells:
    i = i.split(' = ')
    type_of_fire = i[0]
    value_of_cell = int(i[1])

    if water >= value_of_cell:

        if type_of_fire == 'High':
            if 81 <= value_of_cell <= 125:
                water -= value_of_cell
                total_fire += value_of_cell
                effort += value_of_cell * 0.25
                put_on_cells.append(value_of_cell)

        elif type_of_fire == 'Medium':
            if 51 <= value_of_cell <= 80:
                water -= value_of_cell
                total_fire += value_of_cell
                effort += value_of_cell * 0.25
                put_on_cells.append(value_of_cell)

        elif type_of_fire == 'Low':
            if 1 <= value_of_cell <= 50:
                water -= value_of_cell
                total_fire += value_of_cell
                effort += value_of_cell * 0.25
                put_on_cells.append(value_of_cell)

print('Cells:')
for j in put_on_cells:
    print(f' - {j}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
