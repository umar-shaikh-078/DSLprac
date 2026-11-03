n = int(input("Enter number of students: "))

roll = []

for i in range(n):
    r = int(input("Enter roll number: "))
    roll.append(r)

key = int(input("Enter roll number to search: "))

found = False

for i in range(n):

    if roll[i] == key:
        print("Student attended training")
        print("Position:", i + 1)
        found = True
        break

if found == False:
    print("Student did not attend training")