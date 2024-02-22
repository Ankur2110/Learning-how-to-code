class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result =''
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node != self.tail:
                result += '->'
                temp_node = temp_node.next
            else:
                break
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:

            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length +=1 

    def prepend(self, value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:

            self.tail.next = new_node
            new_node.next = self.head
            self.head = new_node
        self.length +=1 


    def insert(self, value, index):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            print("Empty Linked List, element added at zero index")
        elif index == 0:
            self.tail.next = new_node
            new_node.next = self.head
            self.head = new_node
        else: 
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1






CSLL = CSLinkedlist()
# CSLL.append(50)
# CSLL.append(55)

# CSLL.append(99)
# CSLL.append(100)
# CSLL.append(110)
# CSLL.prepend(1001)
# CSLL.insert(20,3)
CSLL.insert(20,0)

print (CSLL)