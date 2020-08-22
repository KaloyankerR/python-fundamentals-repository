import re

pattern = r"(\=|\/)([A-Z]{1}[a-zA-Z]{2,})\1"
data = input()

matches = re.findall(pattern, data)
destinations = []
for match in matches:
    destinations.append(match[1])

print(f"Destinations: {', '.join(destinations)}")

travel_points = 0
for destination in destinations:
    travel_points += len([x for x in destination])


print(f"Travel Points: {travel_points}")
