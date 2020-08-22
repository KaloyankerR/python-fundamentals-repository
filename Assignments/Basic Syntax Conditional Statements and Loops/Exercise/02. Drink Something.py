age = int(input())
message = 'drink '

if age <= 14:
    message += 'toddy'
elif age <= 18:
    message += 'coke'
elif age <= 21:
    message += 'beer'
else:
    message += 'whisky'

print(message)
