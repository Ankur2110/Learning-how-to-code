class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1


    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node != self.tail:
                result += ' <--> '
            temp_node = temp_node.next
        return result
    
Double_list = DLL()
Double_list.append(10)
# Double_list.append(20)
# Double_list.append(30)
# Double_list.append(40)
# Double_list.append(50)
# Double_list.append(60)

print(Double_list)
