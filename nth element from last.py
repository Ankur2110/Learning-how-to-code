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
    
    def nth_element_from_last(self, n):
        target = self.len() - n 
        current_node = self.head
        for _ in range(target):
            current_node = current_node.next
        return current_node

    
ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(8)
ll.append(9)
ll.append(44)
ll.append(65)
ll.append(77)
ll.append(78)
ll.append(89)
ll.append(96)
ll.append(105)
ll.append(200)


print(ll.nth_element_from_last(9))
