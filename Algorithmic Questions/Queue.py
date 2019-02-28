# Queue is a linear data structure with a sequential collection process.

# Python implementation
from collections import deque
class Queue:
    def __init__(self):
        self._queue = deque([])
        
    def add(self.name):
        """
        Add element as the last item in Queue
        """
        self._queue.append(value)
        
    def remove(self):
        """
        Remove elements from the front
        """
        return self._queue.popleft()
    
    def is_empty(self):
        """
        Returns a boolean indication
        """
        return not len(self._queue)
    
    def size(self):
        """
        Return size of the Queue
        """
        return len(self._queue)
    
