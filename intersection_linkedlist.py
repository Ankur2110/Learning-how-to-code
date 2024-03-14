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

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


    def __str__(self):
        values = [str(x.value) for x in self]
        return " -> ".join(values)
    

    def len(self):
        length = 0
        current_node = self.head
        while current_node:
            length +=1
            current_node = current_node.next
        return length
    
    
def intersection(lla, llb):
    if lla.tail != llb.tail:
        return False
    longer = lla if lla.len() > llb.len() else llb
    shorter = llb if lla.len()>llb.len() else lla

    diff = longer.len() - shorter.len()
    shorternode = shorter.head
    longernode = longer.head
    for _ in range(diff):
        longernode = longernode.next
    
    while shorternode != longernode:
        shorternode = shorternode.next
        longernode = longernode.next

    if shorternode == longernode:
        return shorternode
    else:
        return False    
