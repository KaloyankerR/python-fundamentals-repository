chemical_elements = set()

for i in range(int(input())):
    chemical_element = input().split()
    [chemical_elements.add(x) for x in chemical_element if x not in chemical_elements]

print("\n".join(chemical_elements))
