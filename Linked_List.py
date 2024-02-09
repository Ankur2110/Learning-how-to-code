class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail= new_node
#         self.length = 1

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result= ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    
    def insert(self, index, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print ("Linked list is empty, value added at index zero")
        elif index == 0:
            new_node.next = self.head 
            self.head = new_node
        else:
            temp_node = self.head
            for i in range(0, index):
                temp_node = temp_node.next
                if i == (index-2):
                    print ("in loop")
                    new_node.next = temp_node.next
                    temp_node.next = new_node
        self.length += 1

new_LL = LinkedList()
new_LL.append(40)
new_LL.append(20)
new_LL.prepend(101)
new_LL.prepend(121)
new_LL.prepend(131)
new_LL.prepend(141)
new_LL.prepend(151)
new_LL.prepend(1061)
new_LL.prepend(171)

new_LL.insert(0,444)

print (new_LL)

