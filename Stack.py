import unittest
class Item():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack():
    def __init__(self):
        self.head = None

    def pop(self):  
        self.head = self.head.next

    def push(self, data):  
        self.head = Item(data, self.head)

    def peek(self):
        return self.head

    def isEmpty(self):
        return not self.head

class TestStackMethods(unittest.TestCase):
    # Set up for testing the methods of the stack class. Pushes three values to the stack.
    def setUp(self):
        self.newStack = Stack()
        self.newStack.push(0)
        self.newStack.push(1)
        self.newStack.push(2)
        
    def test_peek(self):
        self.assertEqual(self.newStack.peek().data, 2)
    
    def test_Pop(self):
        # After set-up the stack should have a head of 2
        self.assertEqual(self.newStack.peek().data, 2)
        
         # After using the pop method, the new head should be 1
        self.assertEqual(self.newStack.pop(), None)
        self.assertEqual(self.newStack.peek().data, 1)
        
        # After using the pop method, the new head should be 0
        self.assertEqual(self.newStack.pop(), None)
        self.assertEqual(self.newStack.peek().data, 0)
        
    def test_push(self):
        # The current head is 2, after push it should be 3
        self.assertEqual(self.newStack.peek().data, 2)
        self.assertEqual(self.newStack.push(3), None)
        self.assertEqual(self.newStack.peek().data, 3)
        
    def test_isEmpty(self):
        # After set up, the stack has 3 items, after calling pop three times the stack will be empty
        self.assertEqual(self.newStack.isEmpty(), False)
        self.newStack.pop()
        self.newStack.pop()
        self.newStack.pop()
        self.assertEqual(self.newStack.isEmpty(), True)        



if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        