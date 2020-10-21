phone_book = dict()
data = input()

while not data.isnumeric():
    name, phone_number = data.split("-")
    phone_book[name] = phone_number
    data = input()

for i in range(int(data)):
    name = input()

    if name in phone_book.keys():
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")
