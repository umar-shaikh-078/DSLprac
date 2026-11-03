n = int(input("Enter number of members: "))

books = []

for i in range(n):
    b = int(input("Enter books borrowed: "))
    books.append(b)

avg = sum(books) / n

print("Average:", avg)
print("Highest:", max(books))
print("Lowest:", min(books))
print("Zero borrowing:", books.count(0))

freq = {}

for x in books:
    freq[x] = freq.get(x, 0) + 1

mode = max(freq, key=freq.get)

print("Mode:", mode)