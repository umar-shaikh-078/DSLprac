undo_stack = []
redo_stack = []

document = ""

while True:
    print("\n1. Add Text")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_text = input("Enter text to add: ")

        undo_stack.append(document)
        document = document + new_text

        redo_stack.clear()

        print("Text added successfully.")

    elif choice == 2:
        if len(undo_stack) > 0:
            redo_stack.append(document)
            document = undo_stack.pop()
            print("Undo successful.")
        else:
            print("Nothing to undo.")

    elif choice == 3:
        if len(redo_stack) > 0:
            undo_stack.append(document)
            document = redo_stack.pop()
            print("Redo successful.")
        else:
            print("Nothing to redo.")

    elif choice == 4:
        print("Current Document:", document)

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")