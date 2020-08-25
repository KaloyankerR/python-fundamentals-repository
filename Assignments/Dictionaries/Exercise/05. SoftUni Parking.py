n = int(input())
parking_slot = {}

for person in range(n):
    args = input().split(" ")
    command = args[0]
    username = args[1]

    if command == "register":
        plate_number = args[2]
        if username in parking_slot.keys():
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            parking_slot[username] = plate_number
            print(f"{username} registered {plate_number} successfully")

    elif command == "unregister":
        if username not in parking_slot.keys():
            print(f"ERROR: user {username} not found")
        else:
            parking_slot.pop(username)
            print(f"{username} unregistered successfully")

for (k, v) in parking_slot.items():
    print(f"{k} => {v}")
