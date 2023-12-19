#!/usr/bin/python3
""" Module providing a 'Node' class for a singly-linked list
"""


class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
    - __data (int): The data stored in the node.
    - __next_node (Node): Reference to the next node in the linked list.

    Methods:
    - data (property): Getter for retrieving the data.
    - data (setter): Setter for setting the data.
    - next_node (property): Getter for retrieving the next node.
    - next_node (setter): Setter for setting the next node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
        - data (int): The data to be stored in the node.
        - next_node (Node, optional): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for retrieving the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for setting the data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for retrieving the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for setting the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
    - __head (Node): The head node of the linked list.

    Methods:
    - __init__: Initializes a new instance of the SinglyLinkedList class.
    - sorted_insert: Inserts a new Node into the correct sorted position
    - __str__: Returns a string representation of the linked list.
    """

    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
        - str: A string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
