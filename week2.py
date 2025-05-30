# Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. Your implementation should include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: Add a node to the end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as: Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list.
# Singly Linked List implementation using OOP

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        if not curr:
            print("List is empty.")
            return
        while curr:
            print(curr.data, end=" -> " if curr.next else "\n")
            curr = curr.next

    def delete_nth_node(self, n):
        if not self.head:
            print("Error: Cannot delete from an empty list.")
            return
        if n <= 0:
            print("Error: Index should be a positive integer.")
            return
        if n == 1:
            self.head = self.head.next
            return
        curr = self.head
        prev = None
        count = 1
        while curr and count < n:
            prev = curr
            curr = curr.next
            count += 1
        if not curr:
            print("Error: Index out of range.")
            return
        prev.next = curr.next

# Sample usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    print("Original list:")
    ll.print_list()

    print("\nDeleting 3rd node:")
    ll.delete_nth_node(3)
    ll.print_list()

    print("\nDeleting 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTrying to delete 10th node (out of range):")
    ll.delete_nth_node(10)
    ll.print_list()

    print("\nDeleting all nodes:")
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTrying to delete from empty list:")
    ll.delete_nth_node(1)