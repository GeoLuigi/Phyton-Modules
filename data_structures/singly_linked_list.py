"""
Linked list module definition
"""

from python_modules.data_structures.single_node import Node

class SinglyLinkedList:
    """
    Singly linked list class definition
    """
    def __init__(self):
        self.head = None

    def transverse(self):
        """
        Traverse the linked list.
        """
        if self.head is None:
            print("List is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node, end=" -> ")
                current_node = current_node.next

            print("None")

    def insert_at_beg(self, data):
        """
        Insert a node at the head of the list method.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a node at the end of the list method.
        """
        new_node = Node(data)

        # Check if list is empty or not
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert_at_index(self, index, data):
        """
        Insert a node at the given index.
        """
        if index == 1:
            self.insert_at_beg(data)
        else:
            new_node = Node(data)
            current_node = self.head

            position = 1
            while index > position + 1 and current_node is not None:
                current_node = current_node.next
                position += 1

            if current_node is None:
                print("Index out of range")
            else:
                new_node.next = current_node.next
                current_node.next = new_node

    def delete_first_node(self):
        """
        Deletes the first node in the list.
        """
        if self.head is not None:
            self.head = self.head.next

    def delete_last_node(self):
        """
        Deletes the last node in the list.
        """
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                current_node = self.head
                while current_node.next.next is not None:
                    current_node = current_node.next
                current_node.next = None

    def delete_node_by_data(self, data_to_delete):
        """
        Deletes a node with the given data from the list.
        """
        if self.head is not None:
            if self.head.data == data_to_delete:
                self.head = self.head.next
            else:
                current_node = self.head
                while current_node.next is not None and current_node.next.data != data_to_delete:
                    current_node = current_node.next
                if current_node.next is not None:
                    current_node.next = current_node.next.next
