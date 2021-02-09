from linked_list import LinkedList
from stack import Stack


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
    stack.add(0)
    stack.add(1)
    stack.add(2)
    stack.add(3)
    stack.add(-1)
    stack.add(-2)
    stack.add(-3)
    print(stack)

    stack.remove()
    stack.remove()
    print(stack)
    print(stack.top)

    print('-------------------^^ Stack Example ^^-------------------')


if __name__ == '__main__':
    linked_list_example()
    stack_example()