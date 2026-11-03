n = int(input("Enter number of accounts: "))

accounts = []

for i in range(n):
    a = input("Enter account ID: ")
    accounts.append(a)

key = input("Enter ID to search: ")

found = False

for i in range(n):
    if accounts[i] == key:
        print("Account found at position:", i + 1)
        found = True
        break

if found == False:
    print("Account not found")