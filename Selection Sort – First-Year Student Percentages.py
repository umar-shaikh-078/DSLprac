n = int(input("Enter number of students: "))

percentages = []

for i in range(n):
    marks = float(input("Enter percentage: "))
    percentages.append(marks)

# Selection Sort
for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if percentages[j] < percentages[min_index]:
            min_index = j

    percentages[i], percentages[min_index] = percentages[min_index], percentages[i]

print("\nPercentages in ascending order:")
print(percentages)

print("\nTop five percentages:")

for marks in reversed(percentages[-5:]):
    print(marks)