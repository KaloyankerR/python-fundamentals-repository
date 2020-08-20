stops = input()
args = input()

while args != "Travel":
    args = args.split(":")
    cmd = args[0]

    if cmd == "Add Stop":
        index = int(args[1])
        string = args[2]

        if 0 <= index < len(stops):
            stops = [x for x in stops]
            stops.insert(index, string)
            stops = "".join(stops)

    elif cmd == "Remove Stop":
        start_ind = int(args[1])
        end_ind = int(args[2])

        if 0 <= start_ind < len(stops) and 0 <= end_ind < len(stops):
            stops = stops[:start_ind] + stops[end_ind + 1:]

    elif cmd == "Switch":
        old_string = args[1]
        new_string = args[2]

        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)
    args = input()

print(f"Ready for world tour! Planned stops: {stops}")
