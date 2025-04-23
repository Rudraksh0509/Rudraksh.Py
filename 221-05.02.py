nums = [random.randint(1, 10) for _ in range(20)]
target = int(input("Enter number to find: "))
print("Positions:", [i for i, x in enumerate(nums) if x == target])
