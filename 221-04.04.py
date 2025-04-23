def check_number_properties(n):
    
    if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        print("Prime Number")
    else:
        print("Not Prime")

    
    if n == sum(i for i in range(1, n) if n % i == 0):
        print("Perfect Number")
    else:
        print("Not Perfect")

    
    if n == sum(int(d)**len(str(n)) for d in str(n)):
        print("Armstrong Number")
    else:
        print("Not Armstrong")

    
    if str(n) == str(n)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

    
    if str(n**2).endswith(str(n)):
        print("Automorphic Number")
    else:
        print("Not Automorphic")

num = int(input("Enter a number: "))
check_number_properties(num)
