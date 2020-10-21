cars_in_parking = set()

for _ in range(int(input())):
    direction, car_number = input().split(", ")

    if direction == "IN":
        cars_in_parking.add(car_number)
    else:
        cars_in_parking.remove(car_number)

if cars_in_parking:
    print("\n".join(cars_in_parking))
else:
    print("Parking Lot is Empty")
