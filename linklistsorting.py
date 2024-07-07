class Listnode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

value = [2, 3, 4, 5, 6]

def adddata(values):
    dummylist = Listnode(0)  # Create a dummy node with an initial value of 0
    c = dummylist
    for val in values:
        c.next = Listnode(val)
        c = c.next
    return dummylist.next  # Return the actual start of the list

# Create the linked list
linked_list = adddata(value)

# Function to print the linked list for verification
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Print the linked list
print_linked_list(linked_list)
