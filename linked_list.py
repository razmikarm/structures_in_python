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


class LinkedList:

    def __init__(self):
        self.__head = None

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node: Node):
        self.__head = node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next =  Node(data)

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            return
        new_head = Node(data)
        new_head.next, self.head = self.head, new_head
    
    def remove(self, data):
        current = Node('')
        current.next = self.head
        tmp = current
        while current:
            if current.next and current.next.value == data:
                    current.next = current.next.next
            current = current.next
        self.head = tmp.next

    def to_list(self):
        as_list = []
        current = self.head
        while current:
            as_list.append(current.value)
            current = current.next
        return as_list


    def __str__(self):
        return ' -> '.join([str(val) for val in self.to_list()])