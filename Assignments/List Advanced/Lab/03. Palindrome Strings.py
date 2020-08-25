words = input().split(' ')
searched_word = input()

palindromes_words = list(filter(lambda x: x == x[::-1], words))
count = palindromes_words.count(searched_word)

print(palindromes_words)
print(f'Found palindrome {count} times')
