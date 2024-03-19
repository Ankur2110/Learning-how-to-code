class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class queue:

    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.ll ]
        return ' '.join(values)
    
    def enqueue(self, value):
        node = Node(value)
        if self.ll.head ==None:
            self.ll.head = self.ll.tail = node
        else:
            self.ll.tail.next = node
            self.ll.tail = node

    def isempty(self):
        if self.ll.head == None:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.isempty():
            return "The queue is empty"
        else:
            dequeuedNode = self.ll.head
            if self.ll.head == self.ll.tail:
                self.ll.head = self.ll.tail = None
            else:
                self.ll.head = self.ll.head.next
            return dequeuedNode

    def peek(self):
        if self.isempty():
            return "The queue is empty"
        else:
            return self.ll.head.value
        
    def delete(self):
        self.ll.head = self.ll.tail = None



 