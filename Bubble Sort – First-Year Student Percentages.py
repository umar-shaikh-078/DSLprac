n = int(input("Enter number of students: "))

percentages = []

for i in range(n):
    marks = float(input("Enter percentage: "))
    percentages.append(marks)

# Bubble Sort
for i in range(n - 1):
    swapped = False

    for j in range(n - i - 1):
        if percentages[j] > percentages[j + 1]:
            percentages[j], percentages[j + 1] = percentages[j + 1], percentages[j]
            swapped = True

    if not swapped:
        break

print("\nPercentages in ascending order:")
print(percentages)

print("\nTop five percentages:")

for marks in reversed(percentages[-5:]):
    print(marks)