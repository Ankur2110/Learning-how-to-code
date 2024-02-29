class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CDLinkdedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def createCDLL(self, value):
        new_node =  Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        self.length += 1
        return "The CDLL is created successfully"
    
    def insertCDLL(self, value, index):
        temp_node = self.head
        new_node = Node(value)
        if self.head == None:
            return "The CDLL does not exist"
        elif index == 0:
            self.head.prev = new_node
            new_node.next = self.head
            self.tail.next = new_node
            new_node.prev = self.tail
            self.head = new_node 
            self.length += 1
        elif index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.head.prev = new_node
            new_node.next = self.head
            self.tail = new_node
            self.length += 1
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            temp_node.next.prev = new_node
            new_node.next = temp_node.next
            temp_node.next = new_node
            new_node.prev = temp_node
            self.length +=1

    def traverseCDLL(self):
        if self.head == None:
            return "CDLL is empty"
        temp_node = self.head
        while temp_node: 
            print (temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break

    def reverse_traversal(self):
        if self.tail == None:
            return "CDLL is empty"
        temp_node = self.tail
        while temp_node:
            print (temp_node.value)
            temp_node = temp_node.prev
            if temp_node == self.tail:
                break
# Search Circular Doubly Linked List
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value does not exist in CDLL"
                tempNode = tempNode.next
    
    # Delete a node from Circular Doubly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            self.length -= 1
            print("The node has been successfully deleted")
    
    # Delete entire Circular Doubly Linked List
    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
        self.length = 0
        print("The CDLL has been successfully deleted")
    


circularDLL = CDLinkdedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,1)
circularDLL.insertCDLL(1,2)
circularDLL.insertCDLL(2,3)
print([node.value for node in circularDLL])
circularDLL.reverse_traversal()

# circularDLL.deleteCDLL()
# print([node.value for node in circularDLL])




    




            