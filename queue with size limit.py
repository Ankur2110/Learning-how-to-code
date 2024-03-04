class queue:
    
    def __init__(self,maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def isfull(self):
        if self.start ==0 and self.top +1 == self.maxSize:
            return True
        elif self.top +1 == self.start:
            return True
        else: 
            return False
        
    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if self.isfull():
            return "The queue is already full"
        else: 
            if self.top +1 == self.maxSize:
                self.top = 0
            else:
                self.top +=1
                if self.start ==-1:
                    self.start = 0
        self.items[self.top] = value 

    def dequeue(self):
        if self.isempty():
            return "The queue is already empty"
        else:
            firstelement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start +1 == self.maxSize:
                self.start = 0
            else: 
                self.start +=1
            self.items[start] = None
            return firstelement
    
    def peek(self):
        if self.isempty():
            return "Queue is empty"
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items = self.maxSize*[None]
        self.start = -1
        self.top = -1

        






customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.delete()
print(customQueue)