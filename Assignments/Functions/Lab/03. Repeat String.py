def repeat_strings(string, counter):
    result = word * counter
    return result


word = input()
n = int(input())
repeated_string = repeat_strings(word, n)
print(repeated_string)
