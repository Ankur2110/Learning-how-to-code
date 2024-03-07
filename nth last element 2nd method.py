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

def nth_element_from_last(self, n):
    var_1 = self.head
    var_2 = self.head
    for _ in range(n):
        if var_2 is None:
            return None
        var_2 = var_2.next
    while var_2:
        var_1 = var_1.next
        var_2 = var_2.next
    return var_1


