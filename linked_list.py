class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        self.size += 1

    def prepend(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head

        for _ in range(index):
            current = current.next

        return current.value

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head

            for _ in range(index - 1):
                current = current.next

            current.next = current.next.next

        self.size -= 1

    def __len__(self):
        return self.size
