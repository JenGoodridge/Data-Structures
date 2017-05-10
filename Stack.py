class Item():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 
        
class Stack():
    def __init__(self):
        self.head = None
        
    def pop(self): # Remove item from the top of the stack 
        self.head = self.head.next
            
    def push(self, data): #Push new item onto stack
        self.head = Item(data, self.head)
                
    def peek(self): 
        return self.head
        
    def isEmpty(self):
        return self.head == None
    
    
    