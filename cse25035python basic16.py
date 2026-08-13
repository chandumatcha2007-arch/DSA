# Python program to perform Selection Sort

n = int(input("Enter the number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

# Selection Sort
for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j

    # Swap
    a[i], a[min_index] = a[min_index], a[i]

print("Sorted elements are:")
print(a)
