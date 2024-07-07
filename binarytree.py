class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.data))
        if self.left:
            self.left.PrintTree(level + 1, "L--- ")
        if self.right:
            self.right.PrintTree(level + 1, "R--- ")

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(8)
root.insert(13)
root.insert(18)

# Print the tree
root.PrintTree()
