SIZE = 10

EMPTY = None
DELETED = "DELETED"

hash_table = [EMPTY] * SIZE

def hash_function(key):
    return key % SIZE

def insert(key):
    index = hash_function(key)
    first_deleted = -1

    for i in range(SIZE):
        position = (index + i) % SIZE

        if hash_table[position] == key:
            print("Key already exists.")
            return

        if hash_table[position] == DELETED and first_deleted == -1:
            first_deleted = position

        elif hash_table[position] is EMPTY:
            if first_deleted != -1:
                hash_table[first_deleted] = key
            else:
                hash_table[position] = key

            print("Key inserted successfully.")
            return

    if first_deleted != -1:
        hash_table[first_deleted] = key
        print("Key inserted successfully.")
    else:
        print("Hash table is full.")

def search(key):
    index = hash_function(key)

    for i in range(SIZE):
        position = (index + i) % SIZE

        if hash_table[position] is EMPTY:
            print("Key not found.")
            return

        if hash_table[position] == key:
            print("Key found at index:", position)
            return

    print("Key not found.")

def delete(key):
    index = hash_function(key)

    for i in range(SIZE):
        position = (index + i) % SIZE

        if hash_table[position] is EMPTY:
            print("Key not found.")
            return

        if hash_table[position] == key:
            hash_table[position] = DELETED
            print("Key deleted successfully.")
            return

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