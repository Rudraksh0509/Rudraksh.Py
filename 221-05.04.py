nums = [random.randint(-50, 50) for _ in range(30)]
positive = [x for x in nums if x > 0]
negative = [x for x in nums if x < 0]
print("Positive:", positive)
print("Negative:", negative)
    
