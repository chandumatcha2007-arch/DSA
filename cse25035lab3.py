# Recursive function to calculate power
def power(p, n):
    if n == 0:
        return 1
    return p * power(p, n - 1)

# Input Recursive function to calculate power
p = float(input("Enter principal growth factor: "))
n = int(input("Enter number of years: "))

# Calculate power of the  Recursive function
result = power(p, n)

# Output of the recursive function
print("Power (p^n) =", result)




