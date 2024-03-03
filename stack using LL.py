class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None

    def __iter__(self):
        currnode = self.head
        while currnode:
            yield currnode
            currnode = currnode.next


class stack:
    def __init__(self):
        self.linkedlist = LinkedList()
    

    def __str__(self):
        values = [str(x.value) for x in self.linkedlist]
        return '\n'.join(values)
    

    def isempty(self):
        if self.linkedlist.head == None:
            return True
        else: 
            return False
    

    def push(self, value):
        new_node = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head.next = new_node
        else:
            new_node.next = self.linkedlist.head
            self.linkedlist.head = new_node

    def pop(self):
        if self.isempty():
            return "Stack is empty"
        else:
            popped_node = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            return popped_node
        
    def peek(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.linkedlist.head.value
        
    def delete(self):
        self.linkedlist.head = None




        

