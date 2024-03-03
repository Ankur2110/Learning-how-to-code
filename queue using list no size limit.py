class queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isempty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "Item has been inserted at the end of the queue"
    
    def dequeue(self):
        if self.isempty():
            return "Queue is empty"
        else:
            return self.items.pop(0)
            
    def peek(self):
        if self.isempty():
            return "Queue is empty"
        else:
            return self.items[0]
        

    def delete(self):
        self.items =None
        
