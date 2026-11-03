from collections import deque

event_queue = deque()

while True:
    print("\n1. Add Event")
    print("2. Process Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        event = input("Enter event name: ")
        event_queue.append(event)
        print("Event added successfully.")

    elif choice == 2:
        if len(event_queue) > 0:
            event = event_queue.popleft()
            print("Processed Event:", event)
        else:
            print("No events to process.")

    elif choice == 3:
        if len(event_queue) > 0:
            print("Pending Events:", list(event_queue))
        else:
            print("Queue is empty.")

    elif choice == 4:
        event = input("Enter event to cancel: ")

        if event in event_queue:
            event_queue.remove(event)
            print("Event cancelled successfully.")
        else:
            print("Event not found.")

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")