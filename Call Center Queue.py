from collections import deque

call_queue = deque()

def addCall(customerID, callTime):
    call_queue.append((customerID, callTime))
    print("Call added successfully.")

def answerCall():
    if isQueueEmpty():
        print("No calls waiting.")
    else:
        call = call_queue.popleft()
        print("Answered Call:")
        print("Customer ID:", call[0])
        print("Call Time:", call[1])

def viewQueue():
    if isQueueEmpty():
        print("Call queue is empty.")
    else:
        print("Pending Calls:")
        for call in call_queue:
            print("Customer ID:", call[0], "Call Time:", call[1])

def isQueueEmpty():
    return len(call_queue) == 0


while True:
    print("\n1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check Empty")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customerID = input("Enter customer ID: ")
        callTime = input("Enter call time: ")
        addCall(customerID, callTime)

    elif choice == 2:
        answerCall()

    elif choice == 3:
        viewQueue()

    elif choice == 4:
        if isQueueEmpty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")