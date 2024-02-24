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
        while temp_node:
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
        if index ==0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        elif index> self.length or index <0: 
            return "Index out of range"
        else: 
            preceding = self.get(index-1)
            target = preceding.next
            preceding.next = target.next
            target.next = None
            self.length -=1
            return target
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head
        return self
        
    def find_middle(self):
        temp_node = self.head
        index = self.length//2 
        print (index)
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node
    
    def find_middle_1(self):  # "fast and slow pointer" technique or "tortoise and hare" algorithm
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    

    def remove_duplicates(self):
        if self.head is None:
            return self  # If the list is empty, no duplicates to remove
    
        seen = []  # Using a list to keep track of seen values
        current_node = self.head
        length = self.length

        for i in range(length):
            if current_node is None:
                print("Error: Reached end of list unexpectedly.")
                break

            print(f"Processing node with value: {current_node.value}")

            if current_node.value not in seen:
                seen.append(current_node.value)
            else:
                print(f"Duplicate found: {current_node.value}")
                # Remove the duplicate node at index i
                self.remove(i)
            current_node = current_node.next

        return self







    # def remove_duplicates(self):
        
        
    #     if self.head is None:
    #         return self
    #     seen =[]
    #     current_node = self.head
    #     length = self.length
    #     for i in range (length):
    #         if current_node.value not in seen:
    #             seen.append(current_node.value)
    #         else:
    #             self.remove(i)
    #             self.length -=1
    #         current_node = current_node.next
    #     return self
        
        

        
        
    

new_LL = LinkedList()
new_LL.append(40)
new_LL.append(20)
new_LL.prepend(101)
new_LL.prepend(121)
# new_LL.prepend(131)
# new_LL.prepend(141)
# new_LL.prepend(151)
# new_LL.prepend(1061)
# new_LL.prepend(171)
new_LL.append(20)
new_LL.append(20)
new_LL.append(40)
new_LL.append(121)

# new_LL.insert(10,444)


# new_LL.search(2023)
# new_LL.set(5,2121211)
# print (new_LL.pop_first())
# print (new_LL.pop_first())
print (new_LL)
# print(new_LL.remove(0).value)
print (new_LL)

print (new_LL.remove_duplicates())
