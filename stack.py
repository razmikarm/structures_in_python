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
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, node : Node):
        self.__previous = node

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self):
        self.__top = None

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top : Node):
        self.__top = top

    def remove(self):
        self.top = self.top.previous

    def add(self, data):
        new = Node(data)
        new.previous, self.top = self.top, new

    def to_list(self):
        as_list = []
        current = self.top
        while current.previous:
            as_list.append(current.value)
            current = current.previous
        return as_list

    def __str__(self):
        return ' <- '.join([str(val) for val in self.to_list()])
