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


def main():
    ht = HashTable()
    ht.set("name", "Brennon")
    ht.set("age", 18)
    ht.set("major", "Computer Engineering")
    print(ht.get("name"))     # Brennon
    print(ht.get("age"))     # 18
    ht.set("name", "Jacob")  # update existing key
    print(ht.get("name"))    # Jacob
    print(ht.get("missing")) # KeyError


if __name__ == "__main__":
    main()