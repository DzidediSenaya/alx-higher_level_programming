#!/usr/bin/python3
"""
This module contains the Node and SinglyLinkedList classes
"""


class Node:
    """
    Represents a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a node with data and next_node

        Args:
            data: The data to be stored in the node
            next_node (Node): The next node in the linked list
            (default: None)
        Raises:
            TypeError: If data is not an integer
                      If next_node is not None or a Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node

        Returns:
            int: The data stored in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node

        Args:
            value (int): The new data for the node
        Raises:
            TypeError: If data is not an integer
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list

        Returns:
            Node: The next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list

        Args:
            value (Node): The next node in the linked list
        Raises:
            TypeError: If next_node is not None or a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list
    """
    def __init__(self):
        """
        Initializes an empty singly linked list with a head node
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        (increasing order)

        Args:
            value (int): The value to be inserted into the list
        """
        new_node = Node(value)

        if self.head is None:
            # If the list is empty, the new node becomes the head
            self.head = new_node
        elif value < self.head.data:
            # If the value is less than the head's data, insert at the beginning
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                if value > current.next_node.data:
                # Traverse the list to find the correct position for insertion
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list

        Returns:
            str: The string representation of the linked list
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
