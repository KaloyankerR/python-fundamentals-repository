def password_validator(password):
    password_length = 6 <= len(password) <= 10
    password_symbols = True
    for letter in password:
        if letter in '!@#$%^&*()_-=+/|.<>,?\':;':
            password_symbols = False
            break

    password_digits = (sum(digit.isdigit() for digit in password)) >= 2

    if password_length and password_symbols and password_digits:
        print('Password is valid')
    else:
        if not password_length:
            print('Password must be between 6 and 10 characters')
        if not password_symbols:
            print('Password must consist only of letters and digits')
        if not password_digits:
            print('Password must have at least 2 digits')


password_validator(password=input())
