# Python program to perform Insertion Sort

n = int(input("Enter the number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

# Insertion Sort
for i in range(1, n):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j = j - 1

    a[j + 1] = key

print("Sorted elements are:")
print(a)
