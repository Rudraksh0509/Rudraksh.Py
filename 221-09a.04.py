lst = ["madam", "Python", "malayalam", "12321"]

palindromes = list(filter(lambda x: x == x[::-1], lst))
print("Palindromes:", palindromes)
