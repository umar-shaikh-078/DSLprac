n = int(input("Enter number of employees: "))

salaries = []

for i in range(n):
    salary = float(input("Enter salary: "))
    salaries.append(salary)

# Bubble Sort
for i in range(n - 1):
    swapped = False

    for j in range(n - i - 1):
        if salaries[j] > salaries[j + 1]:
            salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
            swapped = True

    if not swapped:
        break

print("\nSalaries in ascending order:")
print(salaries)

print("\nTop five salaries:")

for salary in reversed(salaries[-5:]):
    print(salary)