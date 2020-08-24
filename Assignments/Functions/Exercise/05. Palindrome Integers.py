def palindrome_check(palindrome_numbers):
    for number in palindrome_numbers:
        if number == ''.join(reversed(number)):
            print('True')
        else:
            print('False')


palindrome_check(palindrome_numbers=input().split(', '))
# ''.join(reversed(a))
