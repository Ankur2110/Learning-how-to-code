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
        if index<0 or index > self.length:
            return False
        elif self.head == None:
            self.head = new_node
            self.tail = new_node
            print ("Linked list is empty, value added at index zero")
        elif index == 0:
            new_node.next = self.head 
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1       
        return True
    
    def traverse(self):
        current = self.head
        while current:
            print (current.value)
            current = current.next
    

    def search(self,value):
        current = self.head
        for index in range(self.length):
            if current.value == value:
                print (f"value found at index: {index}")
                return True
            current = current.next
        print ("value not found")

    
    def get(self, index):
        temp_node = self.head
        if index <0 or index > self.length:
            return None
        for i in range(index):
            temp_node = temp_node.next
        return temp_node

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length <=1:
            self.head = None
            self.tail = None
            return "empty Linked list"
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        return temp
    
    def pop(self):
        if self.length <=1:
            self.head = None
            self.tail = None
            return None
        else:
            second_last = self.get(self.length-2)
            last = self.tail
            second_last.next = None
            self.tail = second_last
            self.length -=1
            return last
        
    def remove(self, index):
        if index <1:
            temp = self.pop_first()
            return temp
        elif index> self.length: 
            return "Index out of range"
        else: 
            preceding = self.get(index-1)
            target = preceding.next
            preceding.next = target.next
            target.next = None
            self.length -=1
            return target

        
        # temp_node = self.head
        # if index <0 or index > self.length:
        #     return None
        # for _ in range(index):
        #     temp_node = temp_node.next
        # temp_node.value = value
    

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

# new_LL.insert(10,444)


# new_LL.search(2023)
# new_LL.set(5,2121211)
# print (new_LL.pop_first())
# print (new_LL.pop_first())
print (new_LL)
print(new_LL.remove(0).value)
print (new_LL)
