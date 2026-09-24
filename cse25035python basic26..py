def dequeue(self):
    if self.front==-1 or self.front>self.rear:
        print("Queue underflow")
    else:
        x=self.queue[self.front]
        self.queue[self.front]=None
        self.front+=1
        print(f"{x} deleted from the queue")
queue = []
max_size = int(input("Enter the maximum size of queue: "))

while True:

```
print("\n----------- QUEUE MENU -----------")
print("1. Enqueue")
print("2. Dequeue")
print("3. Peek")
print("4. Display")
print("5. Exit")

choice = int(input("Enter your choice: "))

# ENQUEUE
if choice == 1:

    if len(queue) == max_size:
        print("Queue is Full")

    else:
        value = int(input("Enter the element: "))
        queue.append(value)

        print(value, "inserted into queue")

# DEQUEUE
elif choice == 2:

    if len(queue) == 0:
        print("Queue is Empty")

    else:
        value = queue.pop(0)

        print(value, "deleted from queue")

# PEEK
elif choice == 3:

    if len(queue) == 0:
        print("Queue is Empty")

    else:
        print("Front element is:", queue[0])

# DISPLAY
elif choice == 4:

    if len(queue) == 0:
        print("Queue is Empty")

    else:
        print("Queue elements are:")

        for i in queue:
            print(i, end=" ")

        print()

# EXIT
elif choice == 5:

    print("Exiting Array Queue...")
    break

# INVALID CHOICE
else:
    print("Invalid choice")
```
# NODE CLASS

class Node:

```
def __init__(self, data):
    self.data = data
    self.next = None
```

# Initially queue is empty

front = None
rear = None

while True:
    
print("\n----------- QUEUE MENU -----------")
print("1. Enqueue")
print("2. Dequeue")
print("3. Peek")
print("4. Display")
print("5. Exit")


choice = int(input("Enter your choice: "))

if choice == 1:

    value = int(input("Enter the element: "))

    new_node = Node(value)

    # If queue is empty
    if front is None:

        front = new_node
        rear = new_node

    # If queue is not empty
    else:

        rear.next = new_node
        rear = new_node

    print(value, "inserted into queue")



elif choice == 2:

    if front is None:

        print("Queue is Empty")

    else:

        value = front.data

        front = front.next

        # If queue becomes empty
        if front is None:
            rear = None

        print(value, "deleted from queue")


elif choice == 3:

    if front is None:

        print("Queue is Empty")

    else:

        print("Front element is:", front.data)



elif choice == 4:

    if front is None:

        print("Queue is Empty")

    else:

        temp = front

        print("Queue elements are:")

        while temp is not None:

            print(temp.data, end=" ")

            temp = temp.
```
