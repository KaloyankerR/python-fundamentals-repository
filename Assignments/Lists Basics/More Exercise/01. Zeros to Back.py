elements = input().split(', ')
counter = elements.count('0')

for i in range(counter):
    elements.remove('0')
    elements.append('0')

for j in range(len(elements)):
    elements[j] = int(elements[j])

print(elements)
