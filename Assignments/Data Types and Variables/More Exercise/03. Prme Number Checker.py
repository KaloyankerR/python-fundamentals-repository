number = int(input())
prime = 0

for num in range(2, number):
    if number % num == 0:
        prime += 1
    else:
        pass

if prime:
    print("False")
else:
    print('True')
