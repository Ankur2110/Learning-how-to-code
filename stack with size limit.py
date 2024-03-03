class stack:
    
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        '\n'.join(values)

    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isfull(self):
        if len(self.list) == self.maxsize:
            return True
        else: 
            return f"List not full, {self.maxsize - len(self.list)} items can still be added"
        
    def push(self,value):
        if self.isfull():
            return "Stack is full"
        else:
            self.list.append(value)
            return "The value is added"
        
    def pop(self):
        if self.isempty():
            return "List is already empty"
        else:      
            self.list.pop()
            return "The last element has been popped"
        

    def peek(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.list[-1]
        
    def delete(self):
        self.list = None
    

stack1 = stack(5)

print(stack1.isfull())
