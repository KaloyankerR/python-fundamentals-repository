version = input().split('.')
version = list(map(lambda x: int(x), version))

new_version = version[2] + 1
if new_version > 9:
    version[2] = 0
    new_version = version[1] + 1

    if new_version > 9:
        version[1] = 0
        version[0] += 1
    else:
        version[1] += 1
else:
    version[2] += 1


final_version = [x for x in version]
print(f'{final_version[0]}.{final_version[1]}.{final_version[2]}')
