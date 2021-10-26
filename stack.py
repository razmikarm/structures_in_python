from __future__ import annotations


class Node:

    def __init__(self, value):
        self.__next = None
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node : Node):
        self.__next = node

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self):
        self.__peek = None

    @property
    def peek(self):
        return self.__peek

    @peek.setter
    def peek(self, peek : Node):
        self.__peek = peek

    def pop(self):
        self.peek = self.peek.next

    def push(self, data):
        new = Node(data)
        new.next, self.peek = self.peek, new

    def to_list(self):
        as_list = []
        current = self.peek
        while current:
            as_list.append(current.value)
            current = current.next
        return as_list

    def __str__(self):
        return ' <- '.join([str(val) for val in self.to_list()])
