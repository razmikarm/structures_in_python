from __future__ import annotations


class Node:

    def __init__(self, value):
        self.__previous = None
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


class Queue:

    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, value):
        self.__tail = value

    def add(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new
        if not self.tail:
            self.tail = new

    def remove(self):
        if not self.head.next:
            self.head = None
            self.tail = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        self.tail = current
        current.next = None

    def to_list(self):
        as_list = []
        current = self.head
        while current:
            as_list.append(current)
            current = current.next
        return as_list

    def __str__(self):
        return ' -> '.join([str(var) for var in self.to_list()])