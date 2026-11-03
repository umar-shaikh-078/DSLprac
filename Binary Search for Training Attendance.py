n = int(input("Enter number of students: "))

roll = []

for i in range(n):
    r = int(input("Enter roll number: "))
    roll.append(r)

roll.sort()

print("Sorted roll numbers:", roll)

key = int(input("Enter roll number to search: "))

low = 0
high = n - 1
found = False

while low <= high:

    mid = (low + high) // 2

    if roll[mid] == key:
        print("Student attended training")
        found = True
        break

    elif key < roll[mid]:
        high = mid - 1

    else:
        low = mid + 1

if found == False:
    print("Student did not attend training")