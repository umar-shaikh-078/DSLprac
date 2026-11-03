class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)

    elif key > root.data:
        root.right = insert(root.right, key)

    return root


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    elif key < root.data:
        return search(root.left, key)

    else:
        return search(root.right, key)


def find_min(root):
    current = root

    while current.left is not None:
        current = current.left

    return current


def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Case 3: Two children
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = None

while True:
    print("\n\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter value to insert: "))
        root = insert(root, key)
        print("Value inserted successfully.")

    elif choice == 2:
        key = int(input("Enter value to delete: "))

        if search(root, key):
            root = delete(root, key)
            print("Value deleted successfully.")
        else:
            print("Value not found.")

    elif choice == 3:
        key = int(input("Enter value to search: "))

        if search(root, key):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == 4:
        print("Inorder Traversal:")
        inorder(root)
        print()

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")