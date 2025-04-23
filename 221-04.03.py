text = input("Enter a string: ")
alphabets = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)
print(f"Alphabets: {alphabets}, Digits: {digits}")
