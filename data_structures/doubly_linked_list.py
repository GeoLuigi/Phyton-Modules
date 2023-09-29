"""
Double Linked List Module

This module defines a Doubly Linked List (DLL) data structure, which consists
of nodes that have both next and previous pointers. The DLL can be traversed
forward and backward and supports various insertion and deletion operations.
"""

from data_structures.double_node import DoubleNode

class DoublyLinkedList:
    """
    Doubly linked list class definition
    """
    def __init__(self):
        self.head = None
        self.tail = None

    #Traverse methods

    def transverse_forward(self):
        """
        Traverse the linked list forward.
        """
        current_node = self.head
        while current_node is not None:
            print(current_node, end=" -> ")
            current_node = current_node.next

        print("None")

    def transverse_backward(self):
        """
        Traverse the linked list backward.
        """
        current_node = self.tail
        while current_node is not None:
            print(current_node, end=" -> ")
            current_node = current_node.prev

        print("None")

    #Insertion methods

    def insert_at_index(self, index, data):
        """
        Insert a node at the given index.
        """
        if index < 1:
            # Invalid index, insertion not allowed
            print("Invalid index")
            return

        new_node = DoubleNode(data)

        if index == 1:
            # Insert at the beginning of the list
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return

        current_node = self.head
        position = 1

        while position < index - 1 and current_node is not None:
            current_node = current_node.next
            position += 1

        if current_node is None:
            # Index out of range, insertion not allowed
            print("Index out of range")
            return

        new_node.next = current_node.next
        new_node.prev = current_node
        if current_node.next is not None:
            current_node.next.prev = new_node
        current_node.next = new_node

        if current_node == self.tail:
            self.tail = new_node

    def insert_at_beg(self, data):
        """
        Insert a node at the beginning of the list.
        """
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a node at the end of the list.
        """
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    #Deletion methods

    def delete_node(self, data_to_delete):
        """
        Delete a node with the given data from the list.
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == data_to_delete:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev

                break
            current_node = current_node.next

    def delete_at_beg(self):
        """
        Delete a node at the beginning of the list.
        """
        if self.head is None:
            # The list is empty, there's nothing to delete
            return

        if self.head == self.tail:
            # If there's only one node in the list
            self.head = None
            self.tail = None
        else:
            # If there are more than one nodes in the list
            second_node = self.head.next
            second_node.prev = None
            self.head = second_node


    def delete_at_end(self):
        """
        Delete a node at the end of the list.
        """
        if self.head is None:
            # The list is empty, there's nothing to delete
            return

        if self.head == self.tail:
            # If there's only one node in the list
            self.head = None
            self.tail = None
        else:
            # If there are more than one nodes in the list
            last_node = self.tail
            prev_node = last_node.prev
            prev_node.next = None
            self.tail = prev_node
