class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CDLinkdedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            