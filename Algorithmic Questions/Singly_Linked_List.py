# Singly Linked List
"""A linked list a particular data structure that consist a list of nodes which
Together represent a sequence. In simple terms each node is a data reference
"""

# Python Implementation
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
        
    def set_next(self, next):
        self.next = next
        
    def get_next(self):
        return self.next
        
class SinglyLinkedList:

   def __init__(self):
        self.head = None
        self.size = 0
        
   def add(self, value):
   """
     Time Complexity: 0(N)
     Add element to list
   """
   node = Node(value)
   node.set_next(self.head)
   self.head = node
   self.size = size

return size
   
