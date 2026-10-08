# Binary Tree using Array

class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    # Insert element
    def insert(self, value):
        for i in range(self.size):
            if self.tree[i] is None:
                self.tree[i] = value
                print("Element inserted")
                return
        print("Binary Tree is Full")

    # Preorder Traversal
    def preorder(self, index=0):
        if index < self.size and self.tree[index] is not None:
            print(self.tree[index], end=" ")
            self.preorder(2 * index + 1)
            self.preorder(2 * index + 2)

    # Inorder Traversal
    def inorder(self, index=0):
        if index < self.size and self.tree[index] is not None:
            self.inorder(2 * index + 1)
            print(self.tree[index], end=" ")
            self.inorder(2 * index + 2)

    # Postorder Traversal
    def postorder(self, index=0):
        if index < self.size and self.tree[index] is not None:
            self.postorder(2 * index + 1)
            self.postorder(2 * index + 2)
            print(self.tree[index], end=" ")

    # Search
    def search(self, value):
        if value in self.tree:
            print("Element found")
        else:
            print("Element not found")

    # Display
    def display(self):
        print("Binary Tree:", self.tree)


# Menu
size = int(input("Enter size of Binary Tree: "))
bt = BinaryTree(size)

while True:
    print("\n--- BINARY TREE MENU ---")
    print("1. Insert")
    print("2. Preorder")
    print("3. Inorder")
    print("4. Postorder")
    print("5. Search")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        bt.insert(value)

    elif choice == 2:
        print("Preorder:", end=" ")
        bt.preorder()
        print()

    elif choice == 3:
        print("Inorder:", end=" ")
        bt.inorder()
        print()

    elif choice == 4:
        print("Postorder:", end=" ")
        bt.postorder()
        print()

    elif choice == 5:
        value = int(input("Enter element to search: "))
        bt.search(value)

    elif choice == 6:
        bt.display()

    elif choice == 7:
        print("Program ended")
        break

    else:
        print("Invalid choice")
