n = int(input("Enter number of accounts: "))

accounts = []

for i in range(n):
    a = input("Enter account ID: ")
    accounts.append(a)

accounts.sort()

print("Sorted IDs:", accounts)

key = input("Enter ID to search: ")

low = 0
high = n - 1
found = False

while low <= high:

    mid = (low + high) // 2

    if accounts[mid] == key:
        print("Account found at position:", mid + 1)
        found = True
        break

    elif key < accounts[mid]:
        high = mid - 1

    else:
        low = mid + 1

if found == False:
    print("Account not found")