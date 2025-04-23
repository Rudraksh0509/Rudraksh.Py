import random

nums = {random.randint(15, 45) for _ in range(10)}
print("Original Set:", nums)

less_than_30 = [num for num in nums if num < 30]
print("Numbers less than 30:", len(less_than_30))

nums = {num for num in nums if num <= 35}
print("After removing numbers > 35:", nums)
