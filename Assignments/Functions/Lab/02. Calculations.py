def calculate(operator=input(), num1 = int(input()), num2 = int(input())):
    result = 0
    if operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        result = num1 // num2
    elif operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    return result


print(calculate())
