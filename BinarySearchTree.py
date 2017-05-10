class Node():
    def __init__(self, data, leftChild=None, rightChild=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
          
class BST():
    def __init__(self):
        self.root = None
        self.traversalList = [] 
    
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while current != None: 
                if current.data < data and current.rightChild == None:
                    break
                
                elif current.data > data and current.leftChild == None:
                    break
                       
                elif current.data < data:
                    current = current.rightChild
                
                elif current.data > data:
                    current = current.leftChild 
                
                else:
                    break
            if current.data < data:
                current.rightChild = new_node
            
            elif current.data > data:
                current.leftChild = new_node
            
            else: 
                return False


    def search(self, data):
        current = self.root
        while current != None:
            if current.data == data:
                return current 
            else: 
                if current.data > data: 
                    current = current.leftChild
                else: 
                    current = current.rightChild         
        return None

    def delete(self, data): 
        current = self.root
        previous = self.root
        while current != None: 
            if current.data == data:
                break
            else:
                if current.data > data:
                    previous = current
                    current = current.leftChild
                else: 
                    previous = current
                    current = current.rightChild
            # Case 1 no children at all
        if not current.leftChild and not current.rightChild:
            if previous.data > current.data:
                previous.leftChild = None 
                    
            elif previous == current: 
                self.root = None    
            
            else:
                previous.rightChild = None    
        
        #Case 2: Child on the left none on the right
        
        elif current.leftChild and not current.rightChild:
            if previous.data > current.data:
                previous.leftChild = current.leftChild
                
            elif previous == current: 
                self.root = current.leftChild    
            
            else:
                previous.rightChild = current.leftChild    
        #Case 3: Child on the right none on the left 
    
        elif not current.leftChild and current.rightChild:
            if previous.data > current.data:
                previous.leftChild = current.rightChild
                
            elif previous == current: 
                self.root = current.rightChild    
            
            else:
                previous.rightChild = current.rightChild    
        #Case 4: 2 children
        else:
            if current == self.root:
                self.root = current.leftChild
                new_node = current.rightChild
                current = self.root
                while current.rightChild != None: 
                    current = current.rightChild
                current.rightChild = new_node
                
                
            else:
                if previous.leftChild == current:
                    previous.leftChild = current.leftChild
                else:
                    previous.rightChild = current.leftChild
                
                
                new_node = current.rightChild
                current = current.leftChild
                while current.rightChild != None: 
                    current = current.rightChild
                current.rightChild = new_node
                             

    def preorderTraversal(self):
        _preorderTraversal(self.root)


def _preorderTraversal(node):
    if not node:
        return
    
    print(node.data)    
    _preorderTraversal(node.leftChild)
    _preorderTraversal(node.rightChild)

class Test():
    test = BST()
#    test.AddNode(10)
#    test.AddNode(8)
#    test.AddNode(9)
#    test.AddNode(5)
#    test.AddNode(20)
#    test.AddNode(15)
#    test.AddNode(25)
#    test.deleteNode(20)
    test.insert(10)
    test.insert(5)
    test.insert(3)
    test.insert(7)
    test.insert(20)
    test.insert(15)
    test.insert(30)
    test.preorderTraversal()
                   