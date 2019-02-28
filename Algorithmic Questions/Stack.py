# Definition tech stack
"""
   A stack is using (Last in, First out) is an abstract data type that serves
   as a Collection of elements. Within two prime operations: Push, which adds element to the collection, and pop
   which removes the last element that is added.
"""
# Python Implemtation
class Stack:
    def __init__(self):
        self.stack_list = []
    def add(self, value):
        """
        Adding element at last
        
        Time complexity: 0(1)
        """
        self.stack_list.append(value)
    
    def remove(self):
       """
       Removing an element
       """
    
    def is_empty(self):
      """
      1 value is returned on empty 0 value returned
      """
      
    def size(self):
      """
      Return size of stack
      """
    return len(self.stack_list)
