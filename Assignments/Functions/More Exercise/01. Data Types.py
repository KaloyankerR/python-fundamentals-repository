def data_type(a: str):
    if type_of_input == 'int':
        data = int(input())
        return f'{data * 2}'
    elif type_of_input == 'real':
        data = float(input())
        return f'{data * 1.5:.2f}'
    elif type_of_input == 'string':
        data = input()
        return f'${data}$'


type_of_input = input()
print(data_type(type_of_input))
