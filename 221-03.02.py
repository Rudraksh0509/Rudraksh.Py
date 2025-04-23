def to_lower(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

print(to_lower("Hello PYTHON123"))
