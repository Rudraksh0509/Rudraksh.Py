import random

numbers = [random.randint(-15, 15) for _ in range(10)]
squares = list(map(lambda x: x**2, numbers))

print("Original:", numbers)
print("Squares:", squares)
