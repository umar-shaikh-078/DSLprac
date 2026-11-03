SIZE = 10

hash_table = [[] for i in range(SIZE)]

def hash_function(key):
    return key % SIZE

def insert(key):
    index = hash_function(key)

    if key not in hash_table[index]:
        hash_table[index].append(key)
        print("Key inserted successfully.")
    else:
        print("Key already exists.")

def search(key):
    index = hash_function(key)

    if key in hash_table[index]:
        print("Key found at index:", index)
    else:
        print("Key not found.")

def delete(key):
    index = hash_function(key)

    if key in hash_table[index]:
        hash_table[index].remove(key)
        print("Key deleted successfully.")
    else:
        print("Key not found.")

def display():
    for i in range(SIZE):
        print(i, ":", hash_table[i])


while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        insert(key)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        break

    else:
        print("Invalid choice.")