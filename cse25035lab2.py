# Recursive function to calculate the factorial of a given number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Input of the factorial of the given number
n = int(input("Enter the number of parcels: "))

# Check for negative numbers
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Number of possible arrangements:", factorial(n))
