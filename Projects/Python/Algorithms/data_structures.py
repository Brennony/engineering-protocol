# Brennon York  |  Data Structures  |  9/24/2026


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
        deltax = Node(value)
        if self.head is None:
            self.head = deltax
            return
        x = self.head
        while x.next is not None:
            x = x.next
        x.next = deltax

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

    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next


# Hash Table

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    
    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size
    
    def set(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, k in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        bucket.append((key,value))
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for _, (k,v) in enumerate(bucket):
            if k == key:
                return v
        raise KeyError(key)


# Data Trees

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
            return
        current = self.root
        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def search(self, value):
        if self.root == None:
            return False
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False



# Menu and Case handling

def Menu():
    print("Usable Data Structures:")
    print("1. Stack\n2. Queue\n3. Linked List\n4. Hash Table\n5. Binary Tree")
    while True:
        x = input("\nPlease select a program: ")
        try:
            choice = int(x)
            if choice in (1, 2, 3, 4, 5):
                return choice
        except ValueError:
            pass
        print("Please enter a valid number (1-5).")


def sortInput(choice):
    """Route the menu selection to a demo/test of the matching class."""

    if choice == 1:
        print("\n-- Stack --")
        s = Stack()
        s.push(10)
        s.push(20)
        s.push(30)
        print("Size:", s.size())
        print("Peek:", s.peek())
        print("Pop:", s.pop())
        print("Size after pop:", s.size())
        print("Is empty:", s.is_empty())

    elif choice == 2:
        print("\n-- Queue --")
        q = Queue()
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        print("Size:", q.size())
        print("Peek:", q.peek())
        print("Dequeue:", q.dequeue())
        print("Size after dequeue:", q.size())
        print("Is empty:", q.is_empty())

    elif choice == 3:
        print("\n-- Linked List --")
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        ll.display()
        print("Search 20:", ll.search(20))
        print("Search 99:", ll.search(99))
        ll.delete(20)
        ll.display()

    elif choice == 4:
        print("\n-- Hash Table --")
        ht = HashTable()
        ht.set("a", 1)
        ht.set("b", 2)
        ht.set("a", 99)  # overwrite
        print("a ->", ht.get("a"))
        print("b ->", ht.get("b"))
        try:
            ht.get("z")
        except KeyError:
            print("z -> KeyError raised (expected)")

    elif choice == 5:
        print("\n-- Binary Tree --")
        bst = BST()
        for value in (8, 3, 10, 1, 6, 14):
            bst.insert(value)
        print("Search 6:", bst.search(6))
        print("Search 7:", bst.search(7))
        print("Search 14:", bst.search(14))
        print("Search 99:", bst.search(99))


# Main

def main():
    choice = Menu()
    sortInput(choice)


if __name__ == "__main__":
    main()