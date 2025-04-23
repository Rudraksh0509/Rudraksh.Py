import math

n = int(input("Enter n: "))
r = int(input("Enter r: "))

nCr = math.comb(n, r)
nPr = math.perm(n, r)

print(f"nCr: {nCr}, nPr: {nPr}")
