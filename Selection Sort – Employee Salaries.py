n = int(input("Enter number of employees: "))

salaries = []

for i in range(n):
    salary = float(input("Enter salary: "))
    salaries.append(salary)

# Selection Sort
for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if salaries[j] < salaries[min_index]:
            min_index = j

    salaries[i], salaries[min_index] = salaries[min_index], salaries[i]

print("\nSalaries in ascending order:")
print(salaries)

print("\nTop five salaries:")

for salary in reversed(salaries[-5:]):
    print(salary)