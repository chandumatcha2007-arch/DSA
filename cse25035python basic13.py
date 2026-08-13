# Python program to perform Bubble Sort

n = int(input("Enter the number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            # Swap elements
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted elements are:")
print(a)
