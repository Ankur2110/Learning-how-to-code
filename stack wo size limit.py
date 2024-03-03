class stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isempty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    def pop(self):
        if self.list == []:
            return "Stack is already empty"
        else:
            self.list.pop()
            return "Last element has been removed"
        
    def peek(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.list[-1]
        
    def delete(self):
        self.list = None





stack1 = stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)

print(stack1)

print(stack1.peek())
