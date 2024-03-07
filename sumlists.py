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
        

    def sumList(llA, llB):
        n1 = llA.head
        n2 = llB.head
        carry = 0
        ll = LinkedList()

        while n1 or n2:
            result = carry
            if n1:
                result += n1.value
                n1 = n1.next
            if n2:
                result += n2.value
                n2 = n2.next
            ll.append(int(result % 10))
            carry = result / 10
        
        return ll
