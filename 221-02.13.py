words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
         "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
         "seventeen", "eighteen", "nineteen"]

n = int(input("Enter a number (0-19): "))
if 0 <= n <= 19:
    print(words[n])
else:
    print("Out of range")
