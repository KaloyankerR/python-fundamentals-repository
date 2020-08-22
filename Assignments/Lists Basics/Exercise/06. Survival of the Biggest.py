int_list = input().split(' ')
n = int(input())

for i in range(0, len(int_list)):
    int_list[i] = int(int_list[i])

for i in range(n):
    int_list.remove(min(int_list))

print(int_list)