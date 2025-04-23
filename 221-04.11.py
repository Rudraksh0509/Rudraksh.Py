import math

def sin_x(x, terms=5):
    result = 0
    for i in range(terms):
        sign = (-1)**i
        result += sign * (x**(2*i + 1)) / math.factorial(2*i + 1)
    return result

degree = float(input("Enter angle in degrees: "))
radian = degree * (3.14159 / 180)
print("sin(x) =", sin_x(radian))
