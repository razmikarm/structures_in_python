from linked_list import LinkedList
from stack import Stack
from queue import Queue


def linked_list_example():
    print('------------------->> Linked List Example <<-------------------')
    llist = LinkedList()
    llist.append(0)
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.prepend(-1)
    llist.prepend(-2)
    llist.prepend(-3)
    print(llist)

    llist.remove(2)
    print(llist)

    llist.remove(-3)
    print(llist)

    tmp_node = llist.head
    while tmp_node:
        print(f'| {tmp_node.value} ', end='')
        tmp_node = tmp_node.next
    print('|')

    print(llist.head)

    print('-------------------^^ Linked List Example ^^-------------------')
    print()


def stack_example():
    print('------------------->> Stack Example <<-------------------')
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(-1)
    stack.push(-2)
    stack.push(-3)
    print(stack)

    stack.pop()
    stack.pop()
    print(stack)
    print(stack.peek)

    print('-------------------^^ Stack Example ^^-------------------')
    print()


def queue_example():
    print('------------------->> Queue Example <<-------------------')
    queue = Queue()
    queue.add(3)
    queue.add(2)
    queue.add(1)
    queue.add(0)
    queue.add(-1)
    print(queue)
    queue.remove()
    print(queue)
    queue.remove()
    print(queue)
    print(queue.head)
    print(queue.tail)

    print('-------------------^^ Queue Example ^^-------------------')
    print()


if __name__ == '__main__':
    linked_list_example()
    stack_example()
    queue_example()