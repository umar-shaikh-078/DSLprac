n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = float(input("Enter marks: "))
    marks.append(m)

avg = sum(marks) / n

print("Average marks:", avg)
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Absent students:", marks.count(0))

freq = {}

for x in marks:
    freq[x] = freq.get(x, 0) + 1

mode = max(freq, key=freq.get)

print("Most frequent mark:", mode)