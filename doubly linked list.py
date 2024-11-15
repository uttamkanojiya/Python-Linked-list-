class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.prev = None  # Pointer to the previous node, initially None
        self.next = None  # Pointer to the next node, initially None

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node with the provided data
        if self.head is None:
            self.head = new_node  # If list is empty, set head to the new node
        else:
            new_node.next = self.head  # New node points to the current head
            self.head.prev = new_node  # Current head's previous points to new node
            self.head = new_node  # Update head to the new node

    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node with the provided data
        if self.head is None:
            self.head = new_node  # If list is empty, set head to the new node
        else:
            temp = self.head
            while temp.next:  # Traverse to the end of the list
                temp = temp.next
            temp.next = new_node  # Set the last node's next to the new node
            new_node.prev = temp  # Set the new node's previous to the last node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index cannot be negative.")
            return

        new_node = Node(data)  # Create a new node with the provided data
        temp = self.head
        current_index = 0

        if index == 0:
            self.insert_at_beginning(data)
            return

        while temp is not None and current_index < index:
            temp = temp.next
            current_index += 1

        if temp is None and current_index == index:  # Insert at the end if index is equal to list size
            self.insert_at_end(data)
        elif temp is not None:
            previous_node = temp.prev
            new_node.prev = previous_node
            new_node.next = temp
            if previous_node is not None:
                previous_node.next = new_node
            temp.prev = new_node
        else:
            print(f"Index {index} out of bounds.")

    def delete_node(self, key):
        temp = self.head

        # Traverse to find the node to delete
        while temp is not None:
            if temp.data == key:
                if temp.prev is None:  # Node to delete is the head
                    self.head = temp.next
                    if self.head is not None:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next is not None:  # Node to delete is not the last node
                        temp.next.prev = temp.prev
                return  # Exit after deleting the node
            temp = temp.next

    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def traverse_backward(self):
        temp = self.head
        if temp is None:
            return
        while temp.next:  # Go to the last node
            temp = temp.next
        while temp:  # Traverse backward from the last node
            print(temp.data, end=' ')
            temp = temp.prev
        print()

# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("Traverse forward:")
dll.traverse_forward()  # Output: 20 10 30 40

dll.insert_at_index(2, 25)
print("After inserting 25 at index 2, Traverse forward:")
dll.traverse_forward()  # Output: 20 10 25 30 40

dll.delete_node(30)
print("After deleting 30, Traverse forward:")
dll.traverse_forward()  # Output: 20 10 25 40

