# Brennon York  |  Data Structures  |  9/21/2026


# LIFO vs FIFO 

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(-1)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def is_balanced(s):
    opening = "([{"
    closing = "}])"
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()

    for i in s:
        if i in opening:
            stack.push(i)
        elif i in closing:
            if stack.is_empty():
                return False
            if stack.pop() != pairs[i]:
                return False

    return stack.is_empty()



# Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        x1 = Node(value)
        if self.head is None:
            self.head = x1
            return
        x = self.head
        while x.next is not None:
            x = x.next
        x.next = x1

    def display(self):
        values = []
        x = self.head
        while x is not None:
            values.append(str(x.value))
            x = x.next
        print(", ".join(values))

    def search(self, target):
        x = self.head
        while x is not None:
            if x.value == target: return True
            x = x.next
        return False



def main():
    ll = LinkedList()
    ll.append(3)
    ll.append(7)
    ll.append(12)
    ll.append(99)
    ll.display()              # should print 3, 7, 12, 99
    print(ll.search(12))      # True
    print(ll.search(50))      # False


if __name__ == "__main__":
    main()